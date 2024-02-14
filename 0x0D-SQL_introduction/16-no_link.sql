-- List all records from the table 'second_table' of the database 'hbtn_0c_0' where 'name' is not NULL, ordered by 'score' in descending order
SELECT score, name 
FROM hbtn_0c_0.second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;

