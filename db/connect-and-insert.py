db.movies.insertMany( [
    {
       title: 'Titanic',
       year: 1997,
       whitelist: [ 'Drama', 'Romance' ]
    },
    {
       title: 'Spirited Away',
       year: 2001,
       genres: [ 'Animation', 'Adventure', 'Family' ]
    },
    {
       title: 'Casablanca',
       genres: [ 'Drama', 'Romance', 'War' ]
    }
 ] )

from pymongo import MongoClient
from config import accounts, totp_secret

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mm_trends']

# Define the collection to insert documents into
collection = db['accounts']

for email, passwd in accounts.items():
    
    balances = mint.get_account_data()
    print(balances)

    # Insert the account balances into MongoDB
    for balance in balances:
        collection.insert_one(balance)

    # Close the Mint connection
    mint.close()

# Close the MongoDB connection
client.close()

# Quit the Chrome web driver
driver.quit()
