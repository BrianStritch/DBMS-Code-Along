"""
This is sqlAlchemy's middle level which uses pythonic type expressions
"""

# firstly import the relevant elements of sqlAlchemy

from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
#       The fact that we have 3 slashes here, signifies that our database is hosted locally within our workspace environment.

db = create_engine("postgresql:///chinook")
"""
         After our engine is created, and connected to our database, we need to use the MetaData
         class, which we can save to a variable name of 'meta'.
          The MetaData class will contain a collection of our table objects, and the associated data within those objects.
"""
meta = MetaData(db)

"""

The following sets the tables as variables for each one:

the variables go in here between the meta and the db.connect,

a handy way to check what the column headers is, is to return false from the database ie: SELECT * FROM "Artist" WHERE false;
       this displays the column headers                     ArtistId | Name 
       and any values -- should be blank if false          ----------+------
                                                           (0 rows)

"""
# create variable for "Artist" table
artist_table = Table(
    # within the table you must specify which columns you wish to display and their type:
    #  the format when defining columns, is the column name, followed by the
    #  type of data presented, and then any other optional fields after that.
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String) 
)

# create variable for "Album" table
"""
Then, we have ArtistId as an Integer, but this time, since this is the Album table,
it will not act as our primary key, but instead, as a Foreign Key.
With the ForeignKey, we need to tell it which table and key to point to, so in this case,
it's artist_table.ArtistId, using the table defined above.
"""
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId")) # docstring above refers to this line
)


# create variable for "Track" table

"""
 when you return false the column headings that are returned are as follows:
     TrackId | Name | AlbumId | MediaTypeId | GenreId | Composer | Milliseconds | Bytes | UnitPrice 
    ---------+------+---------+-------------+---------+----------+--------------+-------+-----------
    (0 rows) 

    each column type is set, strings, integers and float for price as it uses decimal
"""

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String, primary_key=False),
    Column("Milliseconds", Integer, primary_key=False),
    Column("Bytes", Integer, primary_key=False),
    Column("UnitPrice", Float, primary_key=False)    
)


# making the connection -- this is how we connect to the database
# we place our queries in this with statement below
with db.connect() as connection:
    
    """
    we are declaring all 6 queries as a variable so we can comment out
     the ones we dont want to use and leave the one we do, 
    for the purpose of demonstration

        Using the Expression Language, all we need to do is 
        apply the .select() method onto our table.
        Now all that's left to do, is run this query using
         the .execute() method from our database connection.

    the additional two queries are tasks set for me to query 
    demonstrating that i know how to use this functionality

    then typing python3     sql-expression.py      in the terminal will run the program
    """
    
    #          query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    #          query 2 - select only the name column from the "Artist" table         
    """
                           this one uses the with_only _columns method
            Even if we want to grab results from a single column, we need to wrap the column selection inside of a list.
                Also, using dot-nation, we need to use ".c" in our selection, which will identify a specific
                column header on the table.
    """
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])


    #          query 3 - select only the Artist "Queen" the "Artist" table
    """
        For query #3, we want to find just the Artist name of "Queen".
        Again, we're selecting from the artist_table, but this time we need to use the .where()
        method, and from the Name column, looking for only "Queen".

        this time you dont use the square brackets
    """
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")


    #           query 4 - select only by "ArtistId" #51 the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)


    #           query 5 - select only by "ArtistId" #51 the "Album" table
    """
    this one is similar to the above ones but is looking in the
     album table rather than the artist table
    """
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    #           query 6 - select all tracks where the composer is "Queen" from the "Track" table
    #select_query = track_table.select().where(track_table.c.Composer == "Queen")

    """
    the next two are my examples
    """

    #           query 7 - select all tracks where the composer is "AC/DC" from the "Track" table
    #select_query = track_table.select().where(track_table.c.Composer == "AC/DC")

    #           query 8 - select the artist name from artist table equal to UB40
    #select_query = artist_table.select().where(artist_table.c.Name == "UB40")

    results = connection.execute(select_query)
    for result in results:
        print(result)

