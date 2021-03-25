select * from employee;
select * from employee where
salary not in (select distinct A.salary from employee as A, employee as B where A.salary < B.Salary);
select max(salary) from employee ;
select count(*) from employee;
select count(distinct job) from employee;
select max(salary + commission) from employee;
select EmpFName from employee where salary = (select max(salary) from employee); -- Only EmpFName will be selected unreferenced position 
select * from employee where salary = (select max(salary) from employee); -- if the nested query was not used, max(salary) command was not getting reference for the table from where it is selected
-- count() , max(), min(), average() the functions for 
select *, max(salary) from employee; -- concatenate the whole string and the max(salary)
select min(salary) from employee;
select sum(salary) from employee; -- summing all the salaries from the table 
select sum(distinct salary) from employee; -- summing all the distinct salaries from the table 
select sum(salary) from employee where job = 'MANAGER';
select job, sum(salary) from employee group by job; 
select job , salary from employee;
select sum(500) from employee where job = 'MANAGER';
select job, avg(commission) from employee where commission > 0 group by job; -- where commission = 0, they are not contributing in  average salary 
select job, avg(commission) from employee group by job;
select avg(commission) from employee;
select * from employee limit 2;
select sum(salary) from (select * from employee limit 2) as A; 
create table employee_test as select * from employee; 
select * from employee_test;
ALTER table employee_test 
add primary key(EmpCode);
select * from employee_test;
-- Quiz 2 
select sum(1) from employee; -- Question 2
select * from employee where salary in (select max(salary) from employee where salary not in (select max(salary) from employee)); -- Question 1
select *, max(salary) as A from employee where salary < (select max(salary) from employee); -- Avirup's Trial 