# to import psycopg2 you type the following into the command line 
# pip3 install psycopg2
# to run the file you may need to initialise the database again with set_pg and psql and then exit and run this file
# to run this file you run it like any python program          --------    python3 sql-psycopg2.py  ----------- in the terminal


import psycopg2  

# connect to database of your choice database
connection = psycopg2.connect(database = "whatever the database name")
#    We are only specifying the name of our database, "chinook", in double-quotes, but you could
#            include additional connection values such as host, username, password, and so on.

# build a curser object of the database
cursor = connection.cursor()

"""
# these queries get put here specifically between the cursor and results
# query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')
#cursor.execute("SELECT * FROM 'Artist'") this is an example that will throw a syntax error because of the single and double quotes

# query 2 - select only the name column from the "Artist" table
#cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only the Artist "Queen" the "Artist" table
#    Since we need to specify a particular record, unfortunately any combination of single or
#        double quotes just won't work. We need to use a Python string placeholder, and then 
#        define the desired string within a list.
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4 - select only by "ArtistId" #51 the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 - select only by "ArtistId" #51 the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6 - select all tracks where the composer is "Queen" from the "Track" table
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# query 7 - select all tracks where the composer is "AC/DC" from the "Track" table
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# query 8 - select all tracks where the test is "AC/DC" from the "Track" table
#cursor.execute('SELECT * FROM "Track" WHERE "test" = %s', ["AC/DC"])

"""


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
#results = cursor.fetchone()


# close the connection
connection.close()

# print results
for result in results:
    print(result)
