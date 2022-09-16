#!/usr/bin/python3

'''
Write a script that lists all `State` objects, and 
corresponding `City` objects, contained in the database `hbtn_0e_101_usa`

    -Your script should take 3 arguments:
    `mysql username`, `mysql password` and `database name`
    -You must use the module `SQLAlchemy`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -You must use only one query to the database
    -You must use the `cities` relationship for all `State` objects
    -Results must be sorted in ascending order by `states.id` and `cities.id`
    -Results must be displayed as they are in the example below
    -Your code should not be executed when imported

<state id>: <state name>
<tabulation><city id>: <city name>

'''


from sys import argv

from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_header = None
    for instance in session.query(City).order_by(City.id):
        state_data = session.query(State).filter_by(id=instance.state_id).one()
        state_name = state_data.name
        if state_header != f"{instance.state_id}: {state_name}":
            print(f"{instance.state_id}: {state_name}")
            state_header = f"{instance.state_id}: {state_name}"
        print(f"\t{instance.id}: {instance.name}")
