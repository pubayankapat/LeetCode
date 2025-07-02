# Write your MySQL query statement below
Select Max(salary) as SecondHighestSalary from Employee where Salary < (select max(salary) from Employee);