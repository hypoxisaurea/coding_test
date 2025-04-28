-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels.
-- Your result cannot contain duplicates.

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(LOWER(CITY), 1) NOT IN ('a', 'e', 'i', 'o', 'u')
AND RIGHT(LOWER(CITY), 1) NOT IN ('a', 'e', 'i', 'o', 'u');