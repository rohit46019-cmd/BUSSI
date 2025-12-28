from pymongo import MongoClient
from config import config

class MongoDB:
    def __init__(self):
        if config.MONGO_URI:
            self.client = MongoClient(config.MONGO_URI)
            self.db = self.client.group_monitor
            self.users = self.db.users
            self.groups = self.db.groups
            self.topics = self.db.topics
        else:
            self.client = None
            self.db = None
    
    def save_user_session(self, user_id, session_string):
        if self.users:
            self.users.update_one(
                {"user_id": user_id},
                {"$set": {"session_string": session_string}},
                upsert=True
            )
    
    def get_user_session(self, user_id):
        if self.users:
            data = self.users.find_one({"user_id": user_id})
            return data.get("session_string") if data else None
        return None
    
    def save_group(self, group_data):
        if self.groups:
            self.groups.update_one(
                {"username": group_data["username"]},
                {"$set": group_data},
                upsert=True
            )
    
    def get_all_groups(self):
        if self.groups:
            return list(self.groups.find())
        return []
    
    def remove_group(self, username):
        if self.groups:
            self.groups.delete_one({"username": username})
    
    def save_topic(self, group_username, topic_id):
        if self.topics:
            self.topics.update_one(
                {"group_username": group_username},
                {"$set": {"topic_id": topic_id}},
                upsert=True
            )
    
    def get_topic_id(self, group_username):
        if self.topics:
            data = self.topics.find_one({"group_username": group_username})
            return data.get("topic_id") if data else None
        return None

db = MongoDB()
