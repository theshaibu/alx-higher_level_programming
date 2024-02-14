-- List all cities and their corresponding states from the 'cities' table in the 'hbtn_0d_usa' database
SELECT cities.id, cities.name AS city_name, states.name AS state_name 
FROM cities 
LEFT JOIN states ON states.id = cities.state_id 
ORDER BY cities.id;

