
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import InsertOne
from bson import Timestamp
import certifi
import json
from task import Task
from typing import Any
import datetime as dt



uri = "mongodb://ADevHD:Pineapple5!@ac-7md8rzd-shard-00-00.2htv2og.mongodb.net:27017,ac-7md8rzd-shard-00-01.2htv2og.mongodb.net:27017,ac-7md8rzd-shard-00-02.2htv2og.mongodb.net:27017/?ssl=true&replicaSet=atlas-z4oj82-shard-0&authSource=admin&appName=ADHDScheduler"


class Database:
    def __init__(self) -> None:
        self.client = MongoClient(uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))
        self.database = self.client.get_database("ADHD_Users")


    def is_able_to_connect(self) -> bool:
        "ping client and if something is received, we know we're connected"
        try:
            client.admin.command('ping')
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

        if does_user_exist(user):
            collection = database.get_collection(user)
            return collection
        else:
            print(f"Unable to find user {user}!")
            return None

    def does_user_exist(self, user_name:str) -> bool:
        print(f'Is user {user_name} in database?', user_name in database.list_collection_names())
        return user_name in database.list_collection_names()
    
    def add_task_to_database(self, task:Task, user:str= 'debug'):
        "from a given task and user, add task to database if user exists"
        if does_user_exist(user_name=user):
            requesting = []
            collection = database.get_collection(user)
            myDict = json.loads(task.convert_task_data_to_json())
            requesting.append(InsertOne(myDict))

            result = collection.bulk_write(requesting)
            print('result', result)

    def convert_entry_to_task(self, entry:dict[str,Any]) -> Task:
        "from an entry inputted by other function, convert entry to task"
        category = dict(entry.get('category'))  #technically could be None 
        deadline = entry.get('deadline')

        if isinstance(deadline, Timestamp):
            deadline = deadline.as_datetime()

        time_to_complete = entry.get('time')
        HOURS = 0
        MINUTES = 1
        SECONDS = 2
        if time_to_complete is not None:
            time_to_complete = [int(time) for time in time_to_complete.split(':')]

            


        
        print('\ncategory', category)
        print('deadline', deadline)
        print('time_to_complete', time_to_complete)
        print(type(deadline))
        print()

        
        
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
            ID = int(entry['ID']) if entry.get("ID") is not None else 0,
            complete = True if entry.get('complete') == 'true' else False,

            category_name = category['name'] if category is not None and category.get('name') is not None else '',
            category_priority = int(category['priority']) if category is not None and category.get('priority') is not None else 0,
            category_ID = int(category['ID']) if category is not None and category.get('ID') is not None else 0,

            deadline = deadline if deadline is not None else dt.datetime(year=2026, month=4, day= 18, hour=23, minute=59), 
            time_to_complete = dt.timedelta(hours = time_to_complete[HOURS], minutes=time_to_complete[MINUTES], seconds=time_to_complete[SECONDS]) if time_to_complete is not None else dt.timedelta(hours=1)
    
        )
    
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

















# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))
database = client.get_database('ADHD_Users')

def get_database(user:str='debug'):
    "get database of user"
    if does_user_exist(user):
        print(f'Found user {user}!')
    else:
        print(f"Unable to find user {user}!")

def does_user_exist(user_name:str) -> bool:
    print(f'Is user {user_name} in database?', user_name in database.list_collection_names())
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

