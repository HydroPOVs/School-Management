import mysql.connector as mysql

from ABC.config import (
    DATABASE_NAME,
    HOSTNAME,
    PASSWORD,
    USERNAME,
    PORT,
)

def initialize():
    # Use a service account.
    # print("Connecting to database.")
    db = mysql.connect(
        host=HOSTNAME,
        user=USERNAME,
        passwd=PASSWORD,
        port=PORT,
        database=DATABASE_NAME
    )
    if not db.is_connected():
        print("Connection Problem")
        print("Please connect to internet")
        return None
    # print("Successfully connected to database...")
    return db