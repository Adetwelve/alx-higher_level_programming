#!/usr/bin/python3
"""a script that prints the State object with the name passed as 
   argument from the database hbtn_0e_6_usa
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

    # query data of all element in the state
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # print query
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
