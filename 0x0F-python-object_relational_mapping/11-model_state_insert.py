#!/usr/bin/python3
""" adds State object “Louisiana” to database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == '__main__':
    # create link to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create all the table associated with Base metadata
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # print new state
    print(new_state.id)
