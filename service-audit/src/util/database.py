from pymongo import MongoClient

from src.util.constant import DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE

# CLIENT DATABASE
client = MongoClient(DATABASE_MONGODB)

# DATABASE
database_audit = client.arcen_audit

# COLLECTIONS
COLLECTION_AUDIT = database_audit[DATABASE_MONGODB_NAME_TABLE]