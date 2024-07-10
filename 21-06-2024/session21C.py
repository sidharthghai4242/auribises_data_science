from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from tabulate import tabulate

class MongoDBHelper:
    def __init__(self, collection="users"):
        uri = "mongodb+srv://sidharthghai48:ghai@cluster0.ycte4p9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        self.db = client['ghai']
        self.collection = self.db[collection]
    
    def insert(self, document):
        result = self.collection.insert_one(document)
        return result
    
    def fetch(self, query=""):
        documents = self.collection.find(query)
        documents_list = list(documents)
        if documents_list:
            headers = documents_list[0].keys()
            rows = [doc.values() for doc in documents_list]
            print(tabulate(rows,headers=headers,tablefmt='grid'))
        else:
            print("No documents found.")
        return documents_list
    
    def delete(self, query=""):
        result = self.collection.delete_one(query)
        print("Deleted document result:", result)
    
    def update(self, document, query=""):
        document_to_update = {'$set': document}
        result = self.collection.update_one(query, document_to_update)
        print("Update result:", result)
