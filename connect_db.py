import psycopg2
import os

def connect_db():
    get_connection = psycopg2.connect(
        host = os.environ.get("DB_HOST"),
        dbname = os.environ.get("DB_NAME"),
        user = os.environ.get("DB_USER"),
        password = os.environ.get("DB_PASSWORD"),
        port = os.environ.get("DB_PORT")
    )
    return get_connection
