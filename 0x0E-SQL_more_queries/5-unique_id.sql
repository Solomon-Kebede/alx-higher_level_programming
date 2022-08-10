-- script that creates the table id_not_null on your MySQL server, id = 1 and unique
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
