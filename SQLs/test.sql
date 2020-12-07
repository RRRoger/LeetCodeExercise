# WRITE your MySQL query STATEMENT below
SELECT Customers.name AS Customers
FROM Customers AS Customers
LEFT JOIN Orders Orders ON Orders.CustomerId = Customers.Id
GROUP BY Customers.Id,
         Customers.name HAVING count(Orders.id) = 0

# WRITE your MySQL query STATEMENT below
SELECT Department.Name AS Department,
       Employee.Name AS Employee,
       temp.Salary AS Salary
FROM Employee Employee LEFT JOIN
  (SELECT max(Salary) AS Salary,
          DepartmentId
   FROM Employee
   GROUP BY DepartmentId) as temp ON temp.DepartmentId = Employee.DepartmentId
LEFT JOIN Department Department ON Department.Id = Employee.DepartmentId
WHERE Employee.Salary = temp.Salary


SELECT Department.Name AS Department,
       Employee.Name AS Employee,
       temp.Salary AS Salary
FROM Department Department LEFT JOIN
  (SELECT max(Salary) AS Salary,
          DepartmentId
   FROM Employee
   GROUP BY DepartmentId) as temp ON temp.DepartmentId = Department.id
LEFT JOIN Employee Employee ON Employee.DepartmentId = Department.id
WHERE Employee.Salary = temp.Salary