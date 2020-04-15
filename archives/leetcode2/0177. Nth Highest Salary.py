CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
     DECLARE M INT;
    set M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary as getNthHighestSalary
      FROM Employee
      order by Salary desc
      limit M,1
  );
END
