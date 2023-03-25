#!/usr/bin/python3
"""Defines a City class
   Inherits from SQLAlchemy Bass and links to MySQL table state
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """ Represents a state column for MySQL table
        __tablename__ (str): The name of MySQl table to store state.
        id (sqlalchemy.Integer): The city's id.
        name (sqlalchemy.String): The city name.
        state_id: Foreeign Key to state.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
