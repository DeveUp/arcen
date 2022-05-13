from bson import ObjectId

from src.model.Audit import Audit

from src.util.persistence.DataBase import COLLECTION_AUDIT
from src.util.persistence.schema.AuditSchema import auditsSerializer

def findById(id: str) -> dict:
    return auditsSerializer(COLLECTION_AUDIT.find_one({"_id": ObjectId(id)}))

def findAll() -> dict:
    return auditsSerializer(COLLECTION_AUDIT.find())

def save(audit: Audit) -> dict:
    _id = COLLECTION_AUDIT.insert_one(dict(audit))
    return auditsSerializer(COLLECTION_AUDIT.find({"_id": _id.inserted_id}))

def update(id: str, audit: Audit) -> dict:
    COLLECTION_AUDIT.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(audit)
    })
    return auditsSerializer(COLLECTION_AUDIT.find({"_id": ObjectId(id)}))

def deleteById(id: str) -> dict:
    COLLECTION_AUDIT.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
