# Write your MySQL query statement below
select s1.Score as Score , (SELECT COUNT(DISTINCT S2.Score)
                            from Scores AS s2
                            where s2.Score>s1.Score
                           )+1 AS Rank  
from Scores as s1
order by s1.Score DESC

