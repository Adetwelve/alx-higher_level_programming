#!/usr/bin/python3
"""Defines a State class
   Inherits from SQLAlchemy Bass and links to MySQL table state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Represents a state column for MySQL table
        __tablename__ (str): The name of MySQl table to store state.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
