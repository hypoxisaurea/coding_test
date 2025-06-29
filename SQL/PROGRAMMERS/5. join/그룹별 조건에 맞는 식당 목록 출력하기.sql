WITH RANKS AS (
    SELECT
        MEMBER_ID,
        RANK() OVER(ORDER BY COUNT(*) DESC) AS RANKING
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
)
SELECT
    M.MEMBER_NAME,
    R.REVIEW_TEXT,
    DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW R
    LEFT OUTER JOIN MEMBER_PROFILE M USING(MEMBER_ID)
    JOIN RANKS RK USING(MEMBER_ID)
WHERE RK.RANKING = 1
ORDER BY REVIEW_DATE, REVIEW_TEXT;