-- creates the MySQL server user user_0d_1, it should have all privileges on your MySQL server
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' IF NOT EXISTS;
GRANT SELECT ON *.* TO user_0d_1@localhost;
