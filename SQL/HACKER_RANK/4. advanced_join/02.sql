-- You are given three tables: Students, Friends and Packages.

-- Students contains two columns: ID and Name.
-- Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend).
-- Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

-- Write a query to output the names of those students whose best friends got offered a higher salary than them.
-- Names must be ordered by the salary amount offered to the best friends.
-- It is guaranteed that no two students got same salary offer.


SELECT S.NAME
FROM STUDENTS S
INNER JOIN FRIENDS F ON S.ID = F.ID
INNER JOIN PACKAGES SP ON S.ID = SP.ID
INNER JOIN PACKAGES FP ON F.FRIEND_ID = FP.ID
WHERE FP.SALARY > SP.SALARY
ORDER BY FP.SALARY;