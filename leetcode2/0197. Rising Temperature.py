# Write your MySQL query statement below

select w1.Id as ID
from Weather as w1, Weather as w2
where DATEDIFF(W1.RecordDate,W2.RecordDate)=1 and w1.Temperature>w2.Temperature
