# Write your MySQL query statement below
select D.Name as Department,E.Name as Employee,E.Salary
from Employee as E
JOIN Department as D
on D.Id=E.DepartmentId 
where (E.Salary,E.DepartmentId) in (
    select max(E1.Salary),E1.DepartmentId
    from Employee as E1
    group by E1.DepartmentId
)
