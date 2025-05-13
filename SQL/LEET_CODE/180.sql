SELECT DISTINCT(num) AS ConsecutiveNums
FROM (
    SELECT
        id,
        num,
        LAG(num) over(order by id) AS prev_num,
        LEAD(num) over(order by id) AS next_num
    FROM LOGS
) AS TB
WHERE num = TB.prev_num
    AND num = TB.next_num;