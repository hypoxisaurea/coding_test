-- Julia asked her students to create some coding challenges.
-- Write a query to print the hacker_id, name, and the total number of challenges created by each student.
-- Sort your results by the total number of challenges in descending order.
-- If more than one student created the same number of challenges, then sort the result by hacker_id.
-- If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

WITH
CHALLENGE_COUNTS AS (
    SELECT H.HACKER_ID, H.NAME, COUNT(*) AS TOTAL
    FROM HACKERS H
    JOIN CHALLENGES C ON H.HACKER_ID = C.HACKER_ID
    GROUP BY H.HACKER_ID, H.NAME
),
MAX_COUNT AS (
    SELECT MAX(TOTAL) AS MAX_TOTAL
    FROM CHALLENGE_COUNTS
),
FILTERED AS (
    SELECT *
    FROM CHALLENGE_COUNTS
    WHERE TOTAL = (SELECT MAX_TOTAL FROM MAX_COUNT)
    OR TOTAL IN (
        SELECT TOTAL
        FROM CHALLENGE_COUNTS
        GROUP BY TOTAL
        HAVING COUNT(*) = 1
    )
)


SELECT *
FROM FILTERED
ORDER BY TOTAL DESC, HACKER_ID;