-- This sql script prepares a mySQL server for the project
-- by creating a db, configuring username and password
-- and settting up priviledges

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating user and configuring username and password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- granting all privileges on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- granting select privileges on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flush priveleges to apply changes
FLUSH PRIVILEGES;
