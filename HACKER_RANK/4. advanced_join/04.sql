-- Samantha interviews many candidates from different colleges using coding challenges and contests.
-- Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id.
-- Exclude the contest from the result if all four sums are 0.

-- Note: A specific contest can be used to screen candidates at more than one college, but each college only holds 1 screening contest.

WITH
TB1 AS (
    SELECT
        CO.CONTEST_ID,
        SUM(S.TOTAL_SUBMISSIONS) AS TS,
        SUM(S. TOTAL_ACCEPTED_SUBMISSIONS) AS TAS
    FROM COLLEGES CO
        JOIN CHALLENGES CH ON CO.COLLEGE_ID = CH.COLLEGE_ID
        JOIN SUBMISSION_STATS S ON CH.CHALLENGE_ID = S.CHALLENGE_ID
    GROUP BY CO.CONTEST_ID
),
TB2 AS (
    SELECT
        CO.CONTEST_ID,
        SUM(V.TOTAL_VIEWS) AS TV,
        SUM(V.TOTAL_UNIQUE_VIEWS) AS TUV
    FROM COLLEGES CO
        JOIN CHALLENGES CH ON CO.COLLEGE_ID = CH.COLLEGE_ID
        JOIN VIEW_STATS V ON CH.CHALLENGE_ID = V.CHALLENGE_ID
    GROUP BY CO.CONTEST_ID
)
SELECT
    CON.CONTEST_ID,
    CON.HACKER_ID,
    CON.NAME,
    TB1.TS,
    TB1.TAS,
    TB2.TV,
    TB2.TUV
FROM CONTESTS CON
    JOIN TB1 ON CON.CONTEST_ID = TB1.CONTEST_ID
    JOIN TB2 ON CON.CONTEST_ID = TB2.CONTEST_ID
WHERE TB1.TS > 0 AND TB1.TAS > 0 AND TB2.TV > 0 AND TB2.TUV > 0
ORDER BY CON.CONTEST_ID ASC;