import pymongo

from tracardi_mongodb_connector.model.configuration import MongoConfiguration


class MongoClient:
    def __init__(self, config: MongoConfiguration):
        self.config = config
        self.client = pymongo.MongoClient(config.uri)

    def find(self, database, collection, query):
        database = self.client[database]
        collection = database.get_collection(collection)
        return collection.find(query)
