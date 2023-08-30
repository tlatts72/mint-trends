from pymongo import MongoClient
from config import accounts, mongo_credentials

client = MongoClient('mongodb://localhost:27017/', username=mongo_credentials["User"],
                     password=mongo_credentials["Password"])
db = client['mint_trends']
collection = db['mint_account_config']

for each in accounts:
    query = {"User": {"$eq": each["User"]}}
    result = collection.find_one_and_replace(query, replacement=each)
    if result:
        print("User Exists")
    else:
        try:
            collection.insert_one(each, session=None, comment=None)
        except:
            print("Issue Connecting to the database")

for x in collection.find():
    print(x)

client.close()
