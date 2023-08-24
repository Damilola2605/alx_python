#!/usr/bin/python3
"""
This is a module that creates python file
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""Create an engine to connect to the MySQL server"""
engine = create_engine('mysql://username:password@localhost:3306/database_name')

"""Create a declarative base"""
Base = declarative_base()
"""Class for state base"""
class State(Base):
    """Define the State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

"""Create tables in the database"""
Base.metadata.create_all(engine)

"""Create a session"""
Session = sessionmaker(bind=engine)
session = Session()

"""Example usage: Creating a new state"""
new_state = State(name='New York')
session.add(new_state)
session.commit()
session.close()
