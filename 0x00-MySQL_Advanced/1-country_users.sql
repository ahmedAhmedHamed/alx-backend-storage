-- creates table users with extra constraints
-- creates table users with extra constraints, doesn't fail if exists.
CREATE TABLE IF NOT EXISTS users (
	id int AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	name varchar(255),
	country ENUM('US','CO','TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY (id),
	UNIQUE (email)
);

