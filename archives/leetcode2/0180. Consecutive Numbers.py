# Write your MySQL query statement below
select distinct l1.Num as ConsecutiveNums
from Logs as l1, Logs as l2,Logs as l3
where l1.Num = l2.Num and l1.Num = l3.Num and l1.Id+1=l2.Id and l1.Id+2=l3.Id
