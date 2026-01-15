import os
from pymongo import MongoClient



def get_collection():
    client = MongoClient(
    host=os.getenv("MONGO_HOST"),
    port=int(os.getenv("MONGO_PORT")),
    username=os.getenv("MONGO_USERNAME"),
    password=os.getenv("MONGO_PASSWORD"),
    authSource=os.getenv("MONGO_AUTH_SOURCE")
    )
    db = client[os.getenv("MONGO_DB")]
    return db["top_threats"]


def insert_to_mongo(result):
    connecting_to_mongo = get_collection()
    connecting_to_mongo.insert_one(result)






























