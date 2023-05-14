import os

DEBUG = os.getenv("DEBUG")
RELOAD = os.getenv("RELOAD")
API_HOST = os.getenv("API_HOST")
API_PORT = int(os.getenv("API_PORT"))

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
