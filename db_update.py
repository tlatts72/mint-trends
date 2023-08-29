import mintapi
from config import accounts, totp_secret
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("headless=new")

# Create a new Chrome web driver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mm_trends']

# Define the collection to insert documents into
collection = db['account_balances']

# Loop through each email account and query account balances
for email, passwd in accounts.items():
    insert = {
        
    }
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
