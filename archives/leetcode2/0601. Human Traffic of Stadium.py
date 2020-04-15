# Write your MySQL query statement below
SELECT DISTINCT(s1.id),s1.visit_date,s1.people
from stadium as s1,stadium as s2,stadium as s3
where s1.people>=100 and s2.people>=100 and s3.people>=100 and (
    (s1.id-s2.id=1 AND s1.id-s3.id=2)
    or
    (s1.id-s2.id=-1 AND s1.id-s3.id=1)
    or
    (s1.id-s2.id=-2 AND s1.id-s3.id=-1)
)
ORDER BY s1.id asc
