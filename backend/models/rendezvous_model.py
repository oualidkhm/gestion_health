from bson.objectid import ObjectId
from mongo_config import get_db

class RendezVousModel:
    @staticmethod
    def create(data: dict) -> str:
        db = get_db()
        result = db.rendezvous.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def find_all() -> list:
        db = get_db()
        return list(db.rendezvous.find())

    @staticmethod
    def find(rdv_id: str) -> dict:
        db = get_db()
        return db.rendezvous.find_one({"_id": ObjectId(rdv_id)})

    @staticmethod
    def update(rdv_id: str, data: dict) -> int:
        db = get_db()
        result = db.rendezvous.update_one(
            {"_id": ObjectId(rdv_id)}, {"$set": data}
        )
        return result.modified_count

    @staticmethod
    def delete(rdv_id: str) -> int:
        db = get_db()
        result = db.rendezvous.delete_one({"_id": ObjectId(rdv_id)})
        return result.deleted_count
