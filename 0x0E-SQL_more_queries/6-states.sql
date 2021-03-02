-- a script that creates the database

CREATE DATABASE IF EXISTS hbtn_0d_usa
CREATE TABLE IF EXISTS states(
    id INT UNIQUE IF NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id) 
);