import os
from sqlalchemy import create_engine

from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

table_name= 'xdr_data'

connection_params = { "host": DB_HOST, "user": DB_USER, "password": DB_PASSWORD,
                    "port": DB_PORT, "database": DB_NAME}

engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")