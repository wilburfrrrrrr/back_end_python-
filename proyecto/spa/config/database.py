import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = '../database.sqlite'
dir_path = os.path.dirname(os.path.realpath(__file__))
path_file = os.path.join(dir_path, sqlite_file_name)
database_url = f'sqlite:///{path_file}'
engine = create_engine(database_url, echo = True)

Session = sessionmaker(bind=engine)

Base = declarative_base()