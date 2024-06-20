-- Print the description of the table first_table
SELECT 
    CONCAT(
        'CREATE TABLE `', 
        TABLE_NAME, 
        '` (\n', 
        GROUP_CONCAT(
            '  `', COLUMN_NAME, '` ', COLUMN_TYPE, 
            IF(IS_NULLABLE = 'NO', ' NOT NULL', ''), 
            IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', COLUMN_DEFAULT), ''), 
            IF(EXTRA = '', '', CONCAT(' ', EXTRA))
            ORDER BY ORDINAL_POSITION SEPARATOR ',\n'
        ), 
        '\n) ENGINE=', ENGINE, 
        ' DEFAULT CHARSET=', TABLE_COLLATION
    ) AS create_table_statement
FROM information_schema.COLUMNS
JOIN information_schema.TABLES 
ON TABLES.TABLE_NAME = COLUMNS.TABLE_NAME
WHERE TABLES.TABLE_NAME = 'first_table'
AND TABLES.TABLE_SCHEMA = DATABASE();
