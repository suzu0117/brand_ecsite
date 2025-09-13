import pyscopg2
import os

def connect_db():
    get_connection = pyscopg2.connect(
        host = os.environ.get("DB_HOST"),
        name = os.environ.get("DB_NAME"),
        user = os.environ.get("DB_USER"),
        password = os.environ.get("DB_POSSWORD"),
        port = os.environ.get("DB_PORT")
    )
    return get_connection
