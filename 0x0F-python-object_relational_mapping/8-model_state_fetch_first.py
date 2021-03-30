#!/usr/bin/python3
"""
lists all State objects from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    fstate = session.query(State).order_by(State.id).first()
    if fstate is None:
        print("Nothing")
    else:
        print("{}: {}".format(fstate.id, fstate.name))
    session.close()
