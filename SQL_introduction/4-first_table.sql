-- This script creates a table named first_table with columns id and name, if it does not already exist
$CREATE TABLE IF NOT EXIST first_table (
    ID INT,
    NAME VARCHAR(256)
);