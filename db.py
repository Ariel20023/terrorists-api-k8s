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

































# class MongoDB:
#     def __init__(self):
#         self.host = os.getenv("MONGO_HOST")
#         self.db_name = os.getenv("MONGO_DB")
#
#         self.client = MongoClient(f"mongodb://{self.host}:27017")
#         self.db = self.client[self.db_name]
#         self.users = self.db.users
#
#     def insert_user(self, user: dict):
#         result = self.users.insert_one(user)
#         return {"inserted_id": str(result.inserted_id)}
#
#     def get_users(self):
#         users = list(self.users.find({}, {"_id": 0}))
#         return users
