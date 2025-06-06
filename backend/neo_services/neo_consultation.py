# neo_services/neo_consultation.py
from neo4j_config import get_driver

class NeoConsult:
    @staticmethod
    def create_relations(cons_id: str, patient_id: str, medecin_id: str, date: str, description: str):
        driver = get_driver()
        if not driver:
            return
        with driver.session() as session:
            session.run(
                """
                MERGE (p:Patient {id: $pid})
                MERGE (m:Medecin {id: $mid})
                CREATE (c:Consultation {id: $cid, date: $date, description: $description})
                CREATE (p)-[:A_EU]->(c)
                CREATE (m)-[:A_FAIT]->(c)
                """,
                pid=patient_id,
                mid=medecin_id,
                cid=cons_id,
                date=date,
                description=description
            )

    @staticmethod
    def delete_relations(cons_id: str):
        driver = get_driver()
        if not driver:
            return
        with driver.session() as session:
            session.run(
                "MATCH (c:Consultation {id: $cid}) DETACH DELETE c",
                cid=cons_id
            )
    @staticmethod
    def get_all_consults_with_relations():
        driver = get_driver()
        if not driver:
            return []
        with driver.session() as session:
            result = session.run(
                """
                MATCH (p:Patient)-[:A_EU]->(c:Consultation)<-[:A_FAIT]-(m:Medecin)
                RETURN
                  p.id AS patient_id,
                  p.name AS patient_name,
                  c.id AS consultation_id,
                  c.date AS date,
                  c.description AS description,
                  m.id AS medecin_id,
                  m.name AS medecin_name
                """
            )
            return [record.data() for record in result]
@staticmethod
def get_consultation_details(cons_id: str):
    driver = get_driver()
    if not driver:
        return {}
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Patient)-[:A_EU]->(c:Consultation {id: $cid})<-[:A_FAIT]-(m:Medecin)
            RETURN 
              p.id AS patient_id, p.name AS patient_name,
              m.id AS medecin_id, m.name AS medecin_name,
              c.id AS consultation_id, c.date AS date, c.description AS description
            """,
            cid=cons_id
        )
        return result.single().data() if result.peek() else {}
