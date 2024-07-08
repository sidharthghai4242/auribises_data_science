
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
class MongoDBHelper:
    def __init__(self,collection='users'):
        uri = "mongodb+srv://sidharthghai48:ghai@cluster0.ycte4p9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        self.db= client['ghai']
        self.collection=self.db[collection]
    
    def insert(self,document):
        self.collection.insert_one(document)
        print("Document inserted in collection: ",self.collection)
    
    def fetch(self,query=""):
        documents=self.collection.find(query)
        return list(documents)