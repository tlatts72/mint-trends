import mintapi
from config import accounts, totp_secret
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyotp

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create a new Chrome web driver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mm_trends']

# Define the collection to insert documents into
collection = db['account_balances']

# Loop through each email account and query account balances
for email, passwd in accounts.items():
    # Get the Authy token
    token = pyotp.TOTP(totp_secret).now()
    print(token)

    # Authenticate with Mint using the Authy token
    mint = mintapi.Mint(
        email=email,
        password=passwd,
        mfa_method="soft-token",
        mfa_token=totp_secret,
        driver=driver
    )

    # Get all account balances
    balances = mint.get_accounts()
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
