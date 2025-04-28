-- P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

-- * 
-- * * 
-- * * * 
-- * * * * 
-- * * * * *

-- Write a query to print the pattern P(20).

SET @NUMBER = 0;

SELECT REPEAT('* ', @NUMBER := @NUMBER+1)
FROM information_schema.tables
LIMIT 20;