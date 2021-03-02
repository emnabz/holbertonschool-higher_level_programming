-- a script that lists all cities contained in the database 

SELECT cities.id, cities.name states.name 
FROM cities
INNEER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;