# firstly import the relevant elements of sqlAlchemy - we copied the first lines from sql-orm.py
# see all notes in sql orm as they are relevant to a lot of this file also

# IMPORTANT --- YOU CANNOT ADD COLUMNS TO AN EXISTING DATABASE

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
class Drifter(base):
    __tablename__ = "Drifters"
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    engine = Column(String)
    race_team = Column(String)
    country = Column(String)

 # instead of conecting to the database directly, we will ask for a session
 # create a new instance of sessionmaker,  then point to our engine (the db), make sure you use capital S for class name
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
"""

"""
session = Session() 

"""
*****************       CREATE         ********************************
"""
# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our programmer table
James_Deane = Drifter(
    make = "NISSAN",
    model = "SILVIA S14.5",
    engine = "2JZ-GTE",
    race_team = "AIMOL RACING",
    country = "IRELAND"
)

Gotcha = Drifter(
    make = "NISSAN",
    model = "SILVIA S15",
    engine = "SR20DET",
    race_team = "NGK",
    country = "RUSSIA"
)
Ken_Nomura = Drifter(
    make = "Nissan",
    model = "Blitz D1 Spec ER34",
    engine = "RB26DETT",
    race_team = "URAS",
    country = "JAPAN"
)
Keichi_Tsuchiya = Drifter(
    make = "TOYOTA",
    model = "AE86",
    engine = "4AGE",
    race_team = "N/A",
    country = "JAPAN"
)
Vaughn_Gitten_Jr = Drifter(
    make = "FORD",
    model = "MUSTANG",
    engine = "FORD BIG BLOCK",
    race_team = "MONSTER",
    country = "USA"
)
Darren_Mc_Namara = Drifter(
    make = "Nissan",
    model = "Silvia S13 SIL80",
    engine = "NASCAR V8",
    race_team = "GROUP D",
    country = "IRELAND"
)
Max_Orido = Drifter(
    make = "TOYOTA",
    model = "GT86",
    engine = "2JZ-GTE",
    race_team = "HKS",
    country = "JAPAN"
)



# add each instance of our programmers to our session

# session.add(James_Deane)
# session.add(Gotcha)
# session.add(Ken_Nomura)
# session.add(Keichi_Tsuchiya)
# session.add(Vaughn_Gitten_Jr)
# session.add(Darren_Mc_Namara)
# session.add(Max_Orido)

# session.commit()

"""
*****************       UPDATE         ********************************
"""

"""
Ideally, we always want to try to use something unique with data retrieval, and that's precisely
where our primary_key is most helpful on a relational database.
If you've been following along exactly on the previous lesson, then your own record
should have the primary_key of number 7. Since we only want one specific record, it's
important to be sure to add the .first() method at the end of our query.
If you don't add the .first() method, then you'll have to use a for-loop to iterate over
the query list, even though it'll only find a single record using that ID.
"""


# updating a single record
"""
#programmer = session.query(Programmer).filter_by(id = 11).first()
#now we use the programmer variiable to define which columns need updating
# programmer.first_name = "Cream"
# programmer.last_name = "Lovelace"
# programmer.famous_for = "Nacker"
# programmer.gender = "M"
"""

# query all programmers
"""
# people = session.query(Programmer)
# for person in people:
#     if person.gender == 'F':
#         person.gender = "Female"
#     elif person.gender == 'M':
#         person.gender = "Male"
#     else:
#         print("Gender not defined yet")
#     session.commit() # this commit is here to commit the updated record on each iteration


# commit our session to the database
#session.commit()  # this is commented out to update the record i want to update

"""


"""
********************************       DELETE         ********************************************
"""


# to delete a sinngle record
"""
# f_name = input("Enter a First name:")
# l_name = input("Enter a Last name:")
# programmer = session.query(Programmer).filter_by(first_name = f_name, last_name = l_name).first()

# # # defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (Y/N)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found!")
"""

# to delete multiple records


    

"""
To delete multiple records you would:

drifters = session.query(Drifter)
for drifter in drifters:
    print('deleted')
    session.delete(drifter)
    session.commit()


make sure if using this in a real-world scenario, to
use defensive programming to confirm deletion first.
"""




"""
*****************       READ         ********************************
"""
# query the database to find all engineers
drifters = session.query(Drifter)
for drifter in drifters:
    print(
        drifter.id,
        #drifter.name,
        drifter.make,
        drifter.model,
        drifter.engine,
        drifter.race_team,
        drifter.country,        
        sep = " | " # charachter used for seperating each value printed
    )