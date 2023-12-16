
db.createUser(
        {
            user: "puffin_username",
            pwd: "puffin_password",
            roles: [
                {
                    role: "readWrite",
                    db: "puffin_db"
                }
            ]
        }
);