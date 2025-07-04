-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard!
-- Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge.
-- Order your output in descending order by the total number of challenges in which the hacker earned a full score.
-- If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

SELECT H.HACKER_ID, H.NAME
FROM HACKERS H
JOIN (
    SELECT S.HACKER_ID, COUNT(DISTINCT S.CHALLENGE_ID) AS SCORE
    FROM SUBMISSIONS S
    JOIN CHALLENGES C ON S.CHALLENGE_ID = C.CHALLENGE_ID
    JOIN DIFFICULTY D ON D.DIFFICULTY_LEVEL = C.DIFFICULTY_LEVEL
    WHERE S.SCORE = D.SCORE
    GROUP BY S.HACKER_ID
    HAVING COUNT(DISTINCT S.CHALLENGE_ID) > 1
) AS SC
ON H.HACKER_ID = SC.HACKER_ID
ORDER BY  SC.SCORE DESC, H.HACKER_ID ASC;