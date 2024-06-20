-- This script lists all records from second_table with a name value in hbtn_0c_0 database
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
