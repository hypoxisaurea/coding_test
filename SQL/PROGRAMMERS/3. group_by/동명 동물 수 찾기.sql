SELECT
    NAME,
    COUNT(*) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
    HAVING COUNT(*) >= 2
ORDER BY NAME;