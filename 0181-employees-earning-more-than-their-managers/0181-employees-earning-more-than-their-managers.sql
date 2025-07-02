# Write your MySQL query statement below
select e.name as Employee from Employee as e join Employee as emp where e.managerId = emp.id and e.salary > emp.salary;