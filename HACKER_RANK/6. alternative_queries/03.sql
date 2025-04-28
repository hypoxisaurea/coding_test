-- Write a query to print all prime numbers less than or equal to 1000.
-- Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space).
-- For example, the output for all prime numbers <= 10 would be:

-- 2&3&5&7

SET @max_depth = 1000;

WITH RECURSIVE
NUMBERS AS (
    SELECT 2 AS N
    UNION ALL
    SELECT N + 1
    FROM NUMBERS
    WHERE N < @max_depth
),
PRIMES AS (
    SELECT N
    FROM NUMBERS
    WHERE NOT EXISTS (
        SELECT 1
        FROM NUMBERS AS DIVISORS
        WHERE DIVISORS.N <= SQRT(NUMBERS.N)
            AND NUMBERS.N % DIVISORS.N = 0
            AND NUMBERS.N != DIVISORS.N
    )
)

SELECT GROUP_CONCAT(N SEPARATOR '&')
FROM PRIMES;