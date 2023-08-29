# db.movies.insertMany( [
#     {
#        title: 'Titanic',
#        year: 1997,
#        whitelist: [ 'Drama', 'Romance' ]
#     },
#     {
#        title: 'Spirited Away',
#        year: 2001,
#        genres: [ 'Animation', 'Adventure', 'Family' ]
#     },
#     {
#        title: 'Casablanca',
#        genres: [ 'Drama', 'Romance', 'War' ]
#     }
#  ] )

from pymongo import MongoClient
from config import accounts

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mm_trends']

# Define the collection to insert documents into
collection = db['accounts']

for each in accounts.items():
   try:
      print(each["User"])
      db.collection.insertOne(each, session=None, comment=None)
   except:
      print("Issue Connecting to the database")

# Close the MongoDB connection
client.close()


