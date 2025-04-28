-- A median is defined as a number separating the higher half of a data set from the lower half.
-- Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.

SELECT ROUND(AVG(LAT_N), 4) AS MEDIAN
FROM (
    SELECT LAT_N, ROW_NUMBER() OVER(ORDER BY LAT_N) AS ROW_NUM, COUNT(LAT_N) OVER() AS TOTAL_ROWS
    FROM STATION
) AS ORDERED
WHERE ROW_NUM BETWEEN (TOTAL_ROWS + 1) / 2 AND (TOTAL_ROWS + 2) / 2;