from pymongo import MongoClient
from src.util.AuditConstant import DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE

client = MongoClient(DATABASE_MONGODB)
db = client.todo_app

COLLECTION_AUDIT = db[DATABASE_MONGODB_NAME_TABLE]