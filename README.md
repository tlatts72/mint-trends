# mint-trends

Connect one or multiple mint accounts into a dashboard to display account balances.

Utilizes mintapi project at https://github.com/mintapi/mintapi


# Step 1
Initialize MongoDB

Configure your user/password as necessary in db/mongo-docker-compose.yml

Verify MongoDB

From inside the container, or if mongosh is installed on your local machine, run `mongosh "mongodb://root:example@localhost:27017"`
1. `Use 
Run `db.createCollection()
# Step 2
