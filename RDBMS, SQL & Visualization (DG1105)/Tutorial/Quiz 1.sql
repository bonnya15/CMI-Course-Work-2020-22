select salary
from Employee
where salary not in (select distinct A.salary from Employee as A, Employee as B where A.salary <B.salary);

select A.salary , B.salary from Employee as A, Employee as B ; 
select A.salary , B.salary from Employee as A , Employee as B where A.Salary < B.salary; 














































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































