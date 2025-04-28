-- We define an employee's total earnings to be their monthly salary*months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table.
-- Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings.
-- Then print these values as  2space-separated integers.

WITH EARNINGS AS (
    SELECT salary * months AS total_earnings
    FROM Employee
)
SELECT MAX(total_earnings), COUNT(*)
FROM EARNINGS
WHERE total_earnings = (
    SELECT MAX(total_earnings) FROM EARNINGS
);