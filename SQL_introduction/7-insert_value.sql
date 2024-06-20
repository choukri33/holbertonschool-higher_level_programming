-- This script inserts a new row with id 89 and name 'Best School' into the table first_table, ensuring no duplication
INSERT INTO first_table (id, name)
VALUES (89, 'Best School')
ON DUPLICATE KEY UPDATE name = VALUES(name);
