from flask import Blueprint, request, jsonify
from bson import ObjectId
from bson.json_util import dumps
from werkzeug.exceptions import NotFound
from neo_services.neo_utilisateur import (
    creer_utilisateur_neo4j,
    get_all_utilisateurs_neo4j,
    get_utilisateur_by_id_neo4j,
    update_utilisateur_neo4j,
    delete_utilisateur_neo4j
)

utilisateur_routes = Blueprint('utilisateur_routes', __name__)
id_counter = 0

def init_routes(app, mongo_db, neo4j_driver):
    utilisateurs_collection = mongo_db["utilisateurs"]

    # Créer un utilisateur
    @utilisateur_routes.route('/utilisateurs/post', methods=['POST'])
    def ajouter_utilisateur():
        global id_counter
        data = request.get_json()
        if not data:
            return jsonify({"message": "Aucune donnée fournie"}), 400

        id_counter += 1
        data['user_id'] = id_counter

        result = utilisateurs_collection.insert_one(data)
        mongo_id = str(result.inserted_id)

        # Sauvegarde dans Neo4j
        creer_utilisateur_neo4j(neo4j_driver, data, mongo_id)
        return jsonify({"message": "Utilisateur ajouté", "user_id": data['user_id']}), 201


    # Obtenir tous les utilisateurs
    @utilisateur_routes.route('/utilisateurs/get', methods=['GET'])
    def get_all_utilisateurs():
        utilisateurs = list(utilisateurs_collection.find())
        return dumps(utilisateurs), 200


    # Obtenir un utilisateur par ID
    @utilisateur_routes.route('/utilisateurs/get/<int:user_id>', methods=['GET'])
    def get_utilisateur(user_id):
        utilisateur = utilisateurs_collection.find_one({"user_id": user_id})
        if not utilisateur:
            raise NotFound("Utilisateur non trouvé")
        return dumps(utilisateur), 200
    
    # Obtenir un utilisateur par email   
    @utilisateur_routes.route('/utilisateurs/email/<email>', methods=['GET'])
    def get_utilisateur_by_email(email):
        utilisateur = utilisateurs_collection.find_one({"email": email})
        if not utilisateur:
            raise NotFound("Utilisateur non trouvé")
        return dumps(utilisateur), 200

    # Mettre à jour un utilisateur par ID
    @utilisateur_routes.route('/utilisateurs/put/<int:user_id>', methods=['PUT'])
    def update_utilisateur(user_id):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Aucune donnée de mise à jour fournie"}), 400

        result = utilisateurs_collection.update_one(
            {"user_id": user_id},
            {"$set": data}
        )

        if result.matched_count == 0:
            raise NotFound("Utilisateur non trouvé")
        
        # Mise à jour dans Neo4j
        update_utilisateur_neo4j(neo4j_driver, user_id, data)

        return jsonify({"message": "Utilisateur mis à jour"}), 200


    # Supprimer un utilisateur par ID
    @utilisateur_routes.route('/utilisateurs/delete/<int:user_id>', methods=['DELETE'])
    def delete_utilisateur(user_id):
        result = utilisateurs_collection.delete_one({"user_id": user_id})
        if result.deleted_count == 0:
            raise NotFound("Utilisateur non trouvé")
        
        # Suppression dans Neo4j
        delete_utilisateur_neo4j(neo4j_driver, user_id)

        return jsonify({"message": "Utilisateur supprimé"}), 200

    # Enregistrement du blueprint dans l'app Flask
    app.register_blueprint(utilisateur_routes)


