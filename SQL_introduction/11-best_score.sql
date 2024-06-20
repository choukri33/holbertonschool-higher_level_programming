-- This script lists records with score >= 10 from second_table in hbtn_0c_0 database, ordered by score (highest first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
