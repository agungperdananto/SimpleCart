import os
from sqlalchemy import create_engine

from sqlalchemy import MetaData

meta = MetaData()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

base_engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}')