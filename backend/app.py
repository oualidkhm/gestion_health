from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from neo4j import GraphDatabase
from routes.utilisateur_routes import init_routes
from backend.db_config import init_mongodb, init_neo4j


app = Flask(__name__)
CORS(app)  # pour autoriser les requêtes du frontend Angular

# Connexion MongoDB
mongo_db = init_mongodb()

# Connexion Neo4j
neo4j_driver = init_neo4j()

# Initialisation des routes
init_routes(app, mongo_db, neo4j_driver)

if __name__ == '__main__':
    app.run(debug=True)
