# mint-trends

Connect one or multiple mint accounts into a dashboard to display account balances.

Utilizes mintapi project at https://github.com/mintapi/mintapi

# Project Requirements before initial release
- Create functional application
- Dockerize the mongodb solution
- Dockerize the python flask application

The application initial release will contain a dashboard that shows the latest data for each account, as well as a whitelisting functionality of specific accounts

# Prerequisites
- Docker installed

# First Steps
1. Initialize MongoDB

- Configure your database user/password as necessary in db/mongo-docker-compose.yml

- Run mongo-docker-compose.yml and ensure the instance is running
```
docker-compose -d db/mongo-docker-compose.yml
```

2. Copy config-example.py to config.py. 
- Give mint account and mongo database information 

3. Run db/mongo-load-mint-accounts.py to insert the given data from config.py


