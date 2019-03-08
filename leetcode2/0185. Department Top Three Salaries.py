# Write your MySQL query statement below
select D.Name as Department ,Etb1.Name as Employee ,Etb1.Salary as Salary
from Employee as Etb1
join Department as D
on Etb1.DepartmentId=D.Id
where (
    select count(distinct Salary)
    from Employee as Etb2
    where Etb2.DepartmentId=Etb1.DepartmentId and Etb2.Salary>Etb1.Salary
)<3;
