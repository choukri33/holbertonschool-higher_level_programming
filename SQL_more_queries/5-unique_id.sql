-- Create the table unique_id with the columns id and name
CREATE TABLE IF NOT EXISTS unique_id 
(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
