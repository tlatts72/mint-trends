from flask import Flask, render_template
from pymongo import MongoClient
from config import mongo_credentials

# Connect to MongoDB
client = MongoClient(host='mongodb://localhost:27017/', username=mongo_credentials["User"],
                     password=mongo_credentials["Password"])
db = client['mint_trends']
collection = db['account_balances']

# Initialize the Flask application
app = Flask(__name__)


# Define the route to display the account balances
@app.route('/')
def display_balances():
    # Get all documents in the account_balances collection
    query = {"Type": {"$eq": "BankAccount"}}
    balances = list(collection.find(query))
    return render_template(template_name_or_list='index.html', balances=balances)


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
