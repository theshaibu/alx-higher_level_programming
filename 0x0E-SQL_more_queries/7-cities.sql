-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table 'cities' in the database
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

