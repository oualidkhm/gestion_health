# neo_services/neo_rendezvous.py
from neo4j_config import get_driver

class NeoRdv:
    @staticmethod
    def create_relations(rdv_id: str, patient_id: str, medecin_id: str, date: str, statut: str):
        driver = get_driver()
        if not driver:
            return
        with driver.session() as session:
            session.run(
                """
                MERGE (p:Patient {id: $pid})
                MERGE (m:Medecin {id: $mid})
                CREATE (r:RendezVous {id: $rid, date: $date, statut: $statut})
                CREATE (p)-[:A_DEMANDE]->(r)
                CREATE (m)-[:A_RECU]->(r)
                """,
                pid=patient_id,
                mid=medecin_id,
                rid=rdv_id,
                date=date,
                statut=statut
            )

    @staticmethod
    def delete_relations(rdv_id: str):
        driver = get_driver()
        if not driver:
            return
        with driver.session() as session:
            session.run(
                "MATCH (r:RendezVous {id: $rid}) DETACH DELETE r",
                rid=rdv_id
            )
# below delete_relations in neo_services/neo_rendezvous.py
    @staticmethod
    def get_all_rdv_with_relations():
        driver = get_driver()
        if not driver:
            return []
        with driver.session() as session:
            result = session.run(
                """
                MATCH (p:Patient)-[:A_DEMANDE]->(r:RendezVous)<-[:A_RECU]-(m:Medecin)
                RETURN
                  p.id AS patient_id,
                  p.name AS patient_name,
                  r.id AS rendezvous_id,
                  r.date AS date,
                  r.statut AS statut,
                  m.id AS medecin_id,
                  m.name AS medecin_name
                """
            )
            return [record.data() for record in result]
