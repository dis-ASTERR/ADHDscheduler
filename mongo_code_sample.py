from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi


uri = "mongodb://ADevHD:Pineapple5!@ac-7md8rzd-shard-00-00.2htv2og.mongodb.net:27017,ac-7md8rzd-shard-00-01.2htv2og.mongodb.net:27017,ac-7md8rzd-shard-00-02.2htv2og.mongodb.net:27017/?ssl=true&replicaSet=atlas-z4oj82-shard-0&authSource=admin&appName=ADHDScheduler"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))

def get_database():
    db = client['sample_mflix']
    col = db['users']
    x = col.find()
    for item in x:
        print(item)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    get_database()

except Exception as e:
    print(e)

