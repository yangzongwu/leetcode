# Write your MySQL query statement below

# Write your MySQL query statement below

select tb1.Request_at as 'Day', ROUND(sum(case
                                            when tb1.Status='completed' then 0
                                            else 1
                                            end)/count(*),2) as 'Cancellation Rate'
from Trips as tb1
inner join Users as tb2
on tb1.Client_Id=tb2.Users_Id and tb2.Banned='No'

where tb1.Request_at between '2013-10-01' and '2013-10-03'
group by tb1.Request_at
order by Day asc;

