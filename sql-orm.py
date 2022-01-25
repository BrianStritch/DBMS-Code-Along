# firstly import the relevant elements of sqlAlchemy

from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
"""
The reason that we no longer need to import the Table class, is because with the ORM,
we're not going to create tables, but instead, we'll be creating Python classes.
These Python classes that we'll create will subclass the declarative_base, meaning that
any class we're making will extend from the main class within the ORM.
"""

# need to import declarative base
from sqlalchemy.ext.declarative import declarative_base

# need to import the session maker class from the orm
from sqlalchemy.orm import sessionmaker

"""
These Python classes that we'll create will subclass the declarative_base, meaning that
any class we're making will extend from the main class within the ORM.
It's the same exact thing for the sessionmaker; instead of making a connection to the database
directly, we'll be asking for a session, which I'll discuss more in a moment.
Exactly in the same way we did on the previous video, we're going to create a new variable
of 'db', and use create_engine to point to our specific database location.
This tells the application that we're using the Postgres server, on a local host since
there are 3 slashes, in order to connect to our Chinook database.
"""

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()
"""
This new 'base' class will essentially grab the metadata that is produced by our database
table schema, and creates a subclass to map everything back to us here within the 'base' variable.
"""

"""
the queries must go here after the base is declared but before the session is declared
"""

# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float) 


 # instead of conecting to the database directly, we will ask for a session
 # create a new instance of sessionmaker,  then point to our engine (the db), make sure you use capital S for class name
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
"""
in order to connect to the database, we have to call Session()
and open an actual session. To do that, we need another variable called
'session', but this time using a lowercase 's', and we set that to equal the new instance
of the Session() from above.
"""
session = Session() 

"""
The last thing we need to do before we can work with our database, is to actually create
the database subclass and generate all metadata. The base variable, given that it's a subclass
from the declarative_base, will now use the .create_all() method from our database metadata.
"""
# creating the database using declarative_base subclass
base.metadata.create_all(db)



#          query 1 - select all records from the "Artist" table
"""
create a new variable called 'artists', and using our existing 'session' instance, we need to use
    the .query() method to query the Artist class. That should simply select everything on the
    table within the Artist class we defined above.

    We then need to iterate over the results found,
    and print each of the columns using dot-notation on our for-loop.
    I'm also going to separate each item using the Python separator, and have them split
    using the vertical-bar, or pipe, with a space on either side.
"""
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

#          query 2 - select only the name column from the "Artist" table         
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)


#          query 3 - select only the Artist "Queen" the "Artist" table
"""
    For query #3, we want to find just the Artist name of "Queen".
    
     this time we use the filter_by method
     we can also use the .first method as there is only one result
"""
# artist = session.query(Artist).filter_by(Name = "Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


#           query 4 - select only by "ArtistId" #51 the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId = 51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")


#           query 5 - select only by "ArtistId" #51 the "Album" table
"""
this one is similar to the above ones but is looking in the
    album table rather than the artist table
"""
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")


#           query 6 - select all tracks where the composer is "Queen" from the "Track" table
# tracks = session.query(Track).filter_by(Composer="Queen")
# for track in tracks:
#     print(
#         track.TrackId, 
#         track.Name, 
#         track.AlbumId, 
#         track.MediaTypeId,
#         track.GenreId,
#         track.Composer,
#         track.Milliseconds,
#         track.Bytes, 
#         track.UnitPrice,
#         sep="\t |"   # i put this tab in here and modified the width to display better in the console.
#         )

   
"""
the next two are my examples
"""

#           query 7 - select all tracks where the composer is "AC/DC" from the "Track" table
# tracks = session.query(Track).filter_by(Composer="AC/DC")
# for track in tracks:
#     print(
#         track.TrackId, 
#         track.Name, 
#         track.AlbumId, 
#         track.MediaTypeId,
#         track.GenreId,
#         track.Composer,
#         track.Milliseconds,
#         track.Bytes, 
#         track.UnitPrice,
#         sep="\t |"   # i put this tab in here and modified the width to display better in the console.
#         )


#           query 8 - select the artist name from artist table equal to UB40
# artist = session.query(Artist).filter_by(Name="UB40").first()
# print(artist.ArtistId, artist.Name, sep=" | ")
