-- Create the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create the cities table if it does not already exist
CREATE TABLE IF NOT EXISTS cities 
(
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
-- Lister toutes les villes de Californie dans la base de données hbtn_0d_usa

SELECT id, name
FROM cities
WHERE state_id = 
	(
	SELECT id
	FROM states
	WHERE name = 'California'
	)
ORDER BY id ASC;