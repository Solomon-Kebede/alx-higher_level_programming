-- creates the MySQL server user user_0d_1, it should have all privileges on your MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT ON *.* TO user_0d_1@localhost;
