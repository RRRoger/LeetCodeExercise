# WRITE your MySQL query STATEMENT below
SELECT name AS Employee
FROM Employee AS emp1
WHERE EXISTS
    ( SELECT id
     FROM Employee AS emp2
     WHERE emp1.ManagerId=emp2.id
       AND emp1.Salary > emp2.Salary )