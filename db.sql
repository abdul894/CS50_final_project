CREATE Table users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username string(255) UNIQUE NOT NULL,
    email string(255) UNIQUE NOT NULL,
    password string(255), NOT NULL
)