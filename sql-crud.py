# firstly import the relevant elements of sqlAlchemy - we copied the first lines from sql-orm.py
# see all notes in sql orm as they are relevant to a lot of this file also

from sqlalchemy import (
    create_engine, Column, Integer, String
)
"""

"""

# need to import declarative base
from sqlalchemy.ext.declarative import declarative_base

# need to import the session maker class from the orm
from sqlalchemy.orm import sessionmaker

"""

"""

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()
"""

"""

# create a class-based model for the "programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

 # instead of conecting to the database directly, we will ask for a session
 # create a new instance of sessionmaker,  then point to our engine (the db), make sure you use capital S for class name
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
"""

"""
session = Session() 

"""
CREATE
"""
# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our programmer table
ada_lovelace = Programmer(
    first_name = 'Ada',
    last_name = 'Lovelace',
    gender = 'F',
    nationality = 'Brittish',
    famous_for = 'First Programmer'
)

alan_turing = Programmer(
    first_name = 'Alan',
    last_name = 'Turing',
    gender = 'M',
    nationality = 'Brittish',
    famous_for = 'Modern Computing'
)
grace_hopper = Programmer(
    first_name = 'Grace',
    last_name = 'Hopper',
    gender = 'F',
    nationality = 'American',
    famous_for = 'COBOL Language'
)
margaret_hamilton = Programmer(
    first_name = 'Margaret',
    last_name = 'Hamilton',
    gender = 'F',
    nationality = 'American',
    famous_for = 'Apollo 11'
)
bill_gates = Programmer(
    first_name = 'Bill',
    last_name = 'Gates',
    gender = 'M',
    nationality = 'American',
    famous_for = 'Microsoft founder'
)
tim_berners_lee = Programmer(
    first_name = 'Tim',
    last_name = 'Berners Lee',
    gender = 'M',
    nationality = 'Brittish',
    famous_for = 'World Wide Web'
)
brian_stritch = Programmer(
    first_name = 'Brian',
    last_name = 'Stritch',
    gender = 'M',
    nationality = 'Irish',
    famous_for = 'best CI student 2022'
)



# add each instance of our programmers to our session
#session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
session.add(brian_stritch)


# commit our session to the database
session.commit()
"""
READ
"""
# query the database to find all engineers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep = " | " # charachter used for seperating each value printed
    )