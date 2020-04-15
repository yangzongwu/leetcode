# Write your MySQL query statement below
delete 
from Person
where Id not in (
    select * from (
        select min(P1.Id) from Person as P1
        group by P1.Email
        ) as P
)

#delete p1 from Person as P1,Person as P2
#where P1.Id>P2.Id and P1.Email=P2.Email
