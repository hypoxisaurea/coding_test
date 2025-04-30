-- You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date.
-- It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row in the table.
-- If the End_Date of the tasks are consecutive, then they are part of the same project.
-- Samantha is interested in finding the total number of different projects completed.

-- Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order.
-- If there is more than one project that have the same number of completion days, then order by the start date of the project.


WITH
MARKED_PROJECTS AS (
    SELECT TASK_ID, START_DATE, END_DATE,
        CASE
            WHEN LAG(END_DATE) OVER (ORDER BY START_DATE) = START_DATE THEN 0
            ELSE 1
        END AS NEW_PROJECT
    FROM PROJECTS
),
PROJECT_GROUPS AS (
    SELECT *, SUM(NEW_PROJECT) OVER (ORDER BY START_DATE ROWS UNBOUNDED PRECEDING) AS PROJECT_GROUP
    FROM MARKED_PROJECTS
),
PROJECT_AGG AS (
    SELECT MIN(START_DATE) AS PROJECT_START, MAX(END_DATE) AS PROJECT_END
    FROM PROJECT_GROUPS
    GROUP BY PROJECT_GROUP
)
SELECT PROJECT_START, PROJECT_END
FROM PROJECT_AGG
ORDER BY DATEDIFF(PROJECT_END, PROJECT_START) ASC, PROJECT_START ASC;