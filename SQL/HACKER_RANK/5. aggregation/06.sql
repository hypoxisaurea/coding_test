-- Query the difference between the maximum and minimum populations in CITY.

SELECT MAX(POPULATION) - MIN(POPULATION) AS POPULATION_DIFFERENCE
FROM CITY;