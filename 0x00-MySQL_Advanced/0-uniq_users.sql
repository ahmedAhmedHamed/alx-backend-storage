-- creates the users table
-- creates the users table
CREATE TABLE IF NOT EXISTS users (
	id int AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	name varchar(255),
	PRIMARY KEY (id),
	UNIQUE (email)
);

