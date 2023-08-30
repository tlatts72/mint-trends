from flask import Flask, render_template
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mm_trends']
collection = db['account_balances']

# Initialize the Flask application
app = Flask(__name__)


# Define the route to display the account balances
@app.route('/')
def display_balances():
    # Get all documents in the account_balances collection
    balances = list(collection.find())
    return render_template(template_name_or_list='index.html', balances=balances)


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
