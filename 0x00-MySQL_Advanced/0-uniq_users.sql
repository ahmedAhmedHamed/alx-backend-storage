-- creates the users table
-- creates the users table
CREATE TABLE users IF NOT EXISTS (
id int, email varchar(255) NOT NULL UNIQUE, name varchar(255),
PRIMARY KEY (id)
);

