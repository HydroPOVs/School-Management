import os
from dotenv import load_dotenv

load_dotenv()

HOSTNAME = os.getenv("HOST", "localhost")
USERNAME = os.getenv("USER", "root")
PASSWORD = os.getenv("PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
PORT = int(os.getenv("PORT", 3306))