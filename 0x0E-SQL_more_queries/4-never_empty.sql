-- a script that creates the table 

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT NOT NULL DEFAULT 1 AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);