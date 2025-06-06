from neo4j import GraphDatabase

driver = None

def init_neo4j():
    global driver
    uri = "neo4j+s://6f418910.databases.neo4j.io" 
    user = "neo4j"
    password = "m1H8eAs4l_ErJZuy7Vo7C0FMYk9qKWXpgKeoPiWjdGM"  # ← replace with actual password
    driver = GraphDatabase.driver(uri, auth=(user, password))

def get_driver():
    return driver
