from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


database = create_engine('sqlite:///users.db',)
Session = sessionmaker(bind=database)
session = Session()

Base = declarative_base()



def create_db():
    Base.metadata.create_all(database)