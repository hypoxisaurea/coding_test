-- The total score of a hacker is the sum of their maximum scores for all of the challenges.
-- Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score.
-- If more than one hacker achieved the same total score, then sort the result by ascending hacker_id.
-- Exclude all hackers with a total score of  from your result.

WITH MAX_SCORES AS (
    SELECT HACKER_ID, CHALLENGE_ID, MAX(SCORE) AS MAX_SCORE
    FROM SUBMISSIONS
    GROUP BY HACKER_ID, CHALLENGE_ID
),
TOTAL_SCORES AS (
    SELECT HACKER_ID, SUM(MAX_SCORE) AS TOTAL_SCORE 
    FROM MAX_SCORES
    GROUP BY HACKER_ID
)
SELECT H.HACKER_ID, H.NAME, T.TOTAL_SCORE
FROM TOTAL_SCORES T
JOIN HACKERS H ON H.HACKER_ID = T.HACKER_ID
WHERE T.TOTAL_SCORE > 0
ORDER BY T.TOTAL_SCORE DESC, H.HACKER_ID ASC;