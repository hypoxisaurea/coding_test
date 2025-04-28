-- P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

-- * * * * * 
-- * * * * 
-- * * * 
-- * * 
-- *

-- Write a query to print the pattern P(20).

WITH RECURSIVE CTE AS (
    SELECT 20 AS N, REPEAT('* ', 20) AS REP
    UNION ALL
    SELECT N-1, REPEAT('* ', N-1) AS REP
    FROM CTE
    WHERE N > 1
)
SELECT REP
FROM CTE;