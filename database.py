
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi


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
        

    def get_collection_of_user_data(user:str):
        "from a given user string, get collection of user info"
        pass

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))
database = client.get_database('ADHD_Users')

def get_database(user:str='debug'):
    "get database of user"

    if does_user_exist(user):
        collection = database.get_collection(user)
        tasks = collection.find()
        for task in tasks:
            for key, value  in task.items():
                print(key, value)
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

