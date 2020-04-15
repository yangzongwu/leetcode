# Write your MySQL query statement below

select E.Name as Employee 
from Employee as E
where E.Salary > (
select M.Salary from Employee as M
    where E.ManagerId =M.Id
)



select E.Name as Employee 
from Employee as E,Employee as M
where E.ManagerId =M.Id and E.Salary >M.Salary 
