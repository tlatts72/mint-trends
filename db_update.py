import mintapi
from datetime import datetime
from config import accounts as config_accounts, mongo_credentials
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

valid_account_types = ["CreditAccount", "BankAccount", "InvestmentAccount"]

def validate_account(account):
    if account["accountStatus"] == "CLOSED":
        return False
    else:
        if account["Whitelist"]:
            if len(account["Whitelist"]) > 0:
                # add logic
                return True
            else:
                return True
        else:
            return True


def mint_pull(credentials):
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("headless=new")
    # Create a new Chrome web driver with the headless option
    driver = webdriver.Chrome(options=chrome_options)
    mint = mintapi.Mint(credentials["User"],
                    credentials["Password"],
                    mfa_method="soft-token",
                    mfa_token=credentials["TOTP"],
                    wait_for_sync=False,
                    use_chromedriver_on_path=True
                    #driver=driver
                    )
    balances = mint.get_account_data()
    mint.close()
    # Quit the Chrome web driver
    driver.quit()
    print(balances)
    return balances


def mongo_upload():
    # Connect to MongoDB "mint_trends" with collection "account_balances"
    client = MongoClient(host='mongodb://localhost:27017/', username=mongo_credentials["User"],
                         password=mongo_credentials["Password"])
    db = client['mint_trends']
    collection = db['account_balances']
    # Loop through each email account and query account balances
    for each in config_accounts:
        balances = mint_pull(each)
        if validate_account(balances):
            if each["Type"] in valid_account_types:
                insert_statement = {"Account_Name": each["name"],"Type": each["Type"], "Balance": each["value"],
                                    "Mint_Last_Update": each["lastUpdatedDate"], "Insert Time": datetime.now()
                                    }
                collection.insert_one(insert_statement)
    # Close the MongoDB connection
    client.close()


if __name__ == "__main__":
    mongo_upload()
