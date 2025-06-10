import uuid

def creer_utilisateur_neo4j(driver, data, mongo_id):
    with driver.session() as session:
        session.run(
            """
            CREATE (u:Utilisateur {
                user_id: $user_id,
                mongo_id: $mongo_id,
                nom: $nom,
                prenom: $prenom,
                email: $email,
                mot_de_passe: $mot_de_passe,
                role: $role
            })
            """,
            user_id=data.get("user_id"),
            mongo_id=mongo_id,
            nom=data.get("nom"),
            prenom=data.get("prenom"),
            email=data.get("email"),
            mot_de_passe=data.get("mot_de_passe"),
            role=data.get("role")
        )

def get_all_utilisateurs_neo4j(driver):
    with driver.session() as session:
        result = session.run("MATCH (u:Utilisateur) RETURN u")
        return [record["u"] for record in result]

def get_utilisateur_by_id_neo4j(driver, user_id):
    with driver.session() as session:
        result = session.run(
            "MATCH (u:Utilisateur {user_id: $user_id}) RETURN u",
            user_id=user_id
        )
        record = result.single()
        return record["u"] if record else None

def update_utilisateur_neo4j(driver, user_id, data):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (u:Utilisateur {mongo_id: $mongo_id})
            SET u.nom = $nom,
                u.prenom = $prenom,
                u.email = $email,
                u.mot_de_passe: $mot_de_passe,
                u.role = $role
            RETURN u
            """,
            user_id=user_id,
            nom=data.get("nom"),
            prenom=data.get("prenom"),
            email=data.get("email"),
            mot_de_passe=data.get("mot_de_passe"),
            role=data.get("role")
        )
        return result.single() is not None

def delete_utilisateur_neo4j(driver, user_id):
    with driver.session() as session:
        result = session.run(
            "MATCH (u:Utilisateur {user_id: $user_id}) DETACH DELETE u RETURN COUNT(u) AS count",
            user_id=user_id
        )
        return result.single()["count"] > 0
