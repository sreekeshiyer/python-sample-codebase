from pymongo import MongoClient
import logging

class MongoDBConnector:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client.get_database()

    def get_data(self, collection_name):
        return self.db[collection_name].find()
