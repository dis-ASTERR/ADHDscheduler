
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import InsertOne
from bson import Timestamp
import certifi
import json
from typing import Any
import datetime as dt
from datetime import UTC
import indexes
from task import Task





uri = "mongodb://ADevHD:Pineapple5!@ac-7md8rzd-shard-00-00.2htv2og.mongodb.net:27017,ac-7md8rzd-shard-00-01.2htv2og.mongodb.net:27017,ac-7md8rzd-shard-00-02.2htv2og.mongodb.net:27017/?ssl=true&replicaSet=atlas-z4oj82-shard-0&authSource=admin&appName=ADHDScheduler"


class Database:
    def __init__(self) -> None:
        self.client = MongoClient(uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))
        self.database = self.client.get_database("ADHD_Users")
      
    
    def query_database(self, 
                       
                    user:str = 'debug',
                        
                    name:str = '', 
                    tags:list[str] = [],
                    points:int = -1,
                    energy:list[int] = [],
                    difficulty:list[int] = [],  #if not blank, takes in two values and puts them in a list - [lowerbound, upper bound]
                    importance:list[int] = [],
                    prerequisites:list[int] = [],
                    requisites:list[int] = [],
                    ID:int = 0,
                    complete:str = '',
                    category_name:str = '',
                    category_priority:int = 0,
                    category_ID:int = 0,

                    deadline = None, 
                    time_to_complete = None,
        ) -> list[Task]:
        """
        Plan of action:
            - take in user and make collection
            - take in data from ui about everything to query.
            - create a json query using data to query database.
                -if certain fields are empty use indexes
        
        """
        list_of_tasks = []
        collection = self.get_collection_from_user(user=user)
        cursor = None
        query_dict = dict()

        if name != '':
            query_dict['name'] = name
        
        if tags != []:
            query_dict['tags'] = {'$all': tags}

        if points > -1:
            query_dict['points'] = points
        
        if energy != []:
            query_dict['energy'] = {'$gt' :energy[0] - 1, '$lt': energy[1] + 1}
 
        if difficulty != []:
            query_dict['difficulty'] = {'$gt' :difficulty[0] - 1, '$lt': difficulty[1] + 1}

        if importance != []:
            query_dict['importance'] = {'$gt' :importance[0] - 1, '$lt': importance[1] + 1}

        if ID != 0:
            query_dict['ID'] = ID

        if complete != '':
            query_dict['complete'] = complete

        if category_name != '' or category_priority != 0 or category_ID != 0:
            category_list = [category_element for category_element in [category_name, category_priority, category_ID] if category_element != '']
            query_dict['category'] = {'$all': category_list}

        if deadline is not None:
            deadline_str = str(deadline)
            deadline_list = deadline_str.split(' ')
            deadline_str = deadline_list[0] + 'T' + deadline_list[1]
            query_dict['deadline'] = deadline_str


        if time_to_complete is not None:
            query_dict['time'] = str(time_to_complete)


        if collection is not None:
            cursor = collection.find(query_dict)

            for entry in cursor:
                task = self.convert_entry_to_task(entry)
                list_of_tasks.append(task)


        return list_of_tasks


    def pick_task_for_user(self, user, current_energy:int):
        list_of_tasks = self.get_all_entries_and_put_them_in_a_list_of_tasks(user)
        task_to_run = None
        val = -1
        for task in list_of_tasks:
            if task is None: continue
            if val < task.calculate_choice_total(current_energy=current_energy):
                val = task.calculate_choice_total(current_energy=current_energy)
                task_to_run = task


        return task_to_run
            
    def set_task_to_complete(self, user:str, task:Task):
        collection = self.get_collection_from_user(user)
        filter = {'name': task.name}
        update_operation = {'$set': {'complete': 'true'}}
        collection.update_one(filter, update_operation)
    
    def is_able_to_connect(self) -> bool:
        "ping client and if something is received, we know we're connected"
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return True

        except Exception as e:
            print(e)
            return False
    
    def print_out_tasks_of_given_collection(self, user='debug'):
        collection = self.get_collection_from_user(user=user)
        if collection is not None:
            tasks = collection.find()
            for task in tasks:
                for key, value in task.items():
                    print(key, end = ' ')
                    if value is not None:
                        print(value)
                    else:
                        print()
                print()
        else:
            print("Unable to find collection.")

    def get_collection_from_user(self, user:str='debug'):
        "from a given user string, get collection of user info"

        if self.does_user_exist(user):
            collection = self.database.get_collection(user)
            return collection
        else:
            print(f'Unable to find user "{user}"!')
            print(f'Creating collection for user "{user}"')
            collection = self.database.create_collection(user)
            return collection

    def does_user_exist(self, user_name:str) -> bool:
        #print(f'Is user {user_name} in database?', user_name in database.list_collection_names())
        return user_name in self.database.list_collection_names()
    
    def add_task_to_database(self, task:Task, user:str= 'debug'):
        "from a given task and user, add task to database if user exists"
        if self.does_user_exist(user_name=user):
            requesting = []
            collection = self.database.get_collection(user)
            myDict = json.loads(task.convert_task_data_to_json())
            requesting.append(InsertOne(myDict))

            result = collection.bulk_write(requesting)
            print('result', result)

    def convert_entry_to_task(self, entry:dict[str,Any]) -> Task:
        "from an entry inputted by other function, convert entry to task"

        category = dict(entry.get('category'))  #technically could be None 
        deadline = entry.get('deadline')
        #print(deadline[:-3])
        format = '%Y-%m-%dT%H:%M:%S'
        deadline = dt.datetime.strptime(deadline[:-6], format)
        deadline = deadline.astimezone(tz=UTC)

        time_to_complete = entry.get('time')
        

        HOURS = 0
        MINUTES = 1
        SECONDS = 2
        if time_to_complete is not None:
            time_to_complete = [int(time) for time in time_to_complete.split(':')]

        
        """print('\ncategory', category)
        print('deadline', deadline)
        print('time_to_complete', time_to_complete)
        print(type(deadline))
        print()"""

        
        try:
            return Task(
                name = entry['name'] if entry.get('name') is not None else '',
                description = entry['description'] if entry.get('description') is not None else '',
                tags = list(entry['tags']) if entry.get('tags') is not None else [],
                points = int(entry['points']) if entry.get('points') is not None else 0,
                energy = int(entry['energy']) if entry.get('energy') is not None else 0,
                difficulty = int(entry['difficulty']) if entry.get('difficulty') is not None else 0,
                importance = int(entry['importance']) if entry.get('importance') is not None else 0,
                prerequisites = [int(item) for item in list(entry['prerequisites'])] if entry.get('prerequisites') is not None else [],
                requisites = [int(item) for item in list(entry['requisites'])] if entry.get('requisites') is not None else [],
                ID = int(entry['ID']) if entry.get("ID") is not '' else 0,
                complete = True if entry.get('complete') == 'true' else False,

                category_name = category['name'] if category is not None and category.get('name') is not None else '',
                category_priority = int(category['priority']) if category is not None and category.get('priority') is not None else 0,
                category_ID = int(category['ID']) if category is not None and category.get('ID') is not None else 0,

                deadline = deadline if deadline is not None else dt.datetime(year=2026, month=4, day= 18, hour=23, minute=59), 
                time_to_complete = dt.timedelta(hours = time_to_complete[HOURS], minutes=time_to_complete[MINUTES], seconds=time_to_complete[SECONDS]) if time_to_complete is not None else dt.timedelta(hours=1)
        
            )
        except: return
    

    def get_all_entries_and_put_them_in_a_list_of_tasks(self, user:str) -> list[Task]:
        task_list = []
        collection = self.get_collection_from_user(user)
        if collection is not None:
            tasks = collection.find()
            for entry in tasks:
                task_list.append(self.convert_entry_to_task(entry))
        else:
            print("Unable to get any entries from database!")
        return task_list


    def test_entry_tast(self):
        collection = self.get_collection_from_user()
        if collection is None:
            raise ValueError('Unable to get collection with user')
        tasks = collection.find()
        for task in tasks:
            print(self.convert_entry_to_task(task))
        


    @staticmethod
    def ticks_to_datetime(ticks):
        "from https://stackoverflow.com/questions/60156295/pymongo-convert-mongodb-date-to-python-datetime"
        return dt.datetime(1, 1, 1) + dt.timedelta(microseconds=ticks / 10)











"""





# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))
database = client.get_database('ADHD_Users')

def get_database(user:str='debug'):
    "get database of user"
    if does_user_exist(user):
        print(f'Found user "{user}"!')
    else:
        print(f"Unable to find user \"{user}\"!")

def does_user_exist(user_name:str) -> bool:
    print(f'Is user "{user_name}" in database?', user_name in database.list_collection_names())
    return user_name in database.list_collection_names()

def sample_database_test():
    
    
    "Sample Databast Test"

    db = client.get_database("sample_mflix")
    print(db)
    col = db.get_collection("movies")
    movies = col.aggregate([
        {
            '$search': {
            "compound": {
                "must" : [
                {
                    "text": {
                    "query": "baseball",
                    "path": "plot"
                    }
                }
                ],
                "mustNot": [
                {
                    "text": {
                    "query": ["Comedy", "Romance"],
                    "path": "genres"
                    }
                }
                ]
            },
            "sort": {
                "released": -1
            }
            }
        }
    ])
    for movie in movies:
        print(movie)

    

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    get_database()

except Exception as e:
    print(e)

"""