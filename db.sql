CREATE Table users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price INTEGER NOT NULL,
    categoryid INTEGER,
    FOREIGN KEY(categoryid) REFERENCES category(id)
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT 
);

CREATE TABLE cart (
    userid INTEGER,
    productid INTEGER,
    FOREIGN KEY(userid) REFERENCES users(id),
    FOREIGN KEY(productid) REFERENCES product(id)
);