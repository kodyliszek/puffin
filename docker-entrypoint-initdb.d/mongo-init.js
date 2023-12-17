db = db.getSiblingDB("puffin_db")
db.createUser(
    {
        user: "puffin_username",
        pwd: "puffin_password",
        roles: [{role: "readWrite", db: "puffin_db"}],
    }
)
db.createCollection("consumption_data")
db.createCollection("report")


db = db.getSiblingDB("puffin_db_test")
db.createUser(
    {
        user: "puffin_username",
        pwd: "puffin_password",
        roles: [{role: "readWrite", db: "puffin_db_test"}],
    }
)
db.createCollection("consumption_data")
db.createCollection("report")
