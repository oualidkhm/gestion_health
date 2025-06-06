from flask_pymongo import PyMongo

mongo = PyMongo()

def init_mongo(app):
    app.config["MONGO_URI"] = "mongodb+srv://admin:LuTUDs7Ht22F9vhx@cluster0.bgygfpw.mongodb.net/medical_db"
    mongo.init_app(app)

def get_db():
    return mongo.db
