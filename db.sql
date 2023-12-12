CREATE Table users (
    id INTEGER AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    type TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE product (
    id INTEGER AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price INTEGER NOT NULL,
    PRIMARY KEY(id)
    FOREIGN KEY(categoryid) REFERENCES category(id)
);

CREATE TABLE category (
    id INTEGER AUTOINCREMENT,
    name TEXT 
);

CREATE TABLE cart (
    FOREIGN KEY(id) REFERENCES users(id),
    FOREIGN KEY(product) REFERENCES product(id)
);