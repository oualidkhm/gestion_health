from bson.objectid import ObjectId
from mongo_config import get_db

class ConsultationModel:
    @staticmethod
    def create(data: dict) -> str:
        db = get_db()
        result = db.consultations.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def find_all() -> list:
        db = get_db()
        return list(db.consultations.find())

    @staticmethod
    def find(cons_id: str) -> dict:
        db = get_db()
        return db.consultations.find_one({"_id": ObjectId(cons_id)})

    @staticmethod
    def update(cons_id: str, data: dict) -> int:
        db = get_db()
        result = db.consultations.update_one(
            {"_id": ObjectId(cons_id)}, {"$set": data}
        )
        return result.modified_count

    @staticmethod
    def delete(cons_id: str) -> int:
        db = get_db()
        result = db.consultations.delete_one({"_id": ObjectId(cons_id)})
        return result.deleted_count
