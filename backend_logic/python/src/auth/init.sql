CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth123';

CREATE DATABASE AUTH;

GRANT ALL PRIVILEGES ON AUTH.* TO 'auth_user'@'localhost';

USE AUTH;

CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password)
VALUES('ranjan@email', 'Admin123');