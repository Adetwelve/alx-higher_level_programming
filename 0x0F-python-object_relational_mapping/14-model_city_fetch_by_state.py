#!/usr/bin/python3
"""Lists all State objects from database hbtn_0e_6_us
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
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
    query = session.query(City, State)
    states = query.filter(City.state_id == State.id).order_by(City.id)

    # print query
    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
