use assignment;
show tables;

select * from stock;

select distinct symbol from stock;

select * from stock where symbol = 'APOLLOHOSP' and Dates = '2017-11-08';
select ClosePrice from stock where symbol = 'APOLLOHOSP' and Dates = '2017-11-08';

use shiuli;
select * from sample1;
insert into sample1 values(4, 'Anubhab(Baal)', 'A', 2);
insert into sample1 values(4, 'Madhavan', 'A', 2000000);

update sample1
set s_name = 'Baal'
where s_name = 'Anubhab(Baal)';

update sample1 
set grade = 'D'
where grade = 'A';

select * from sample1;
select distinct(roll_num), s_name, grade, p_money from sample1;
select distinct* from sample1;

-- This is an error. Distinct should be put in the 1st column selection 
select roll_num, distinct s_name, grade, p_money from sample1;
select distinct(s_name), roll_num, grade, p_money from sample1;

create table sample2(id INT , Name char(30));
select * from sample2;

drop table sample2;

select * from employee;

select * from employee where job = binary 'MANAGER';  -- Binary for Case sensitive 

select sum(Salary + Commission) from Employee;
select avg(Salary + Commission) from Employee;
select max(Salary) from Employee;

select * from employee where salary =  (select max(salary) from employee);

select count(EmpFname) from employee where salary <= 5000;

select Job, sum(salary + commission) , sum(commission) from employee group by job;

select a.EmpFname, a.job, a.Salary from employee as a inner join (select job, max(salary) as 'salary' from employee group by job) as b where a.job = b.job and a.salary = b.salary;

select * from course;

select * from prereq;


select * from course inner join prereq using(course_id);
select a.course_id, a.title, a.dept_name, a.credits, ifnull(b.prereq_id, 'Math-101') as 'prereq_id' from course as a left join prereq as b using(course_id);

select * from course right join prereq using(course_id);
select * from prereq left join course using(course_id);

select * from course cross join prereq;
select * from course as a cross join course as b;


-- Quiz 4
create table emp(emp_id INT, emp_name VARCHAR(20), department VARCHAR(20), email VARCHAR(20), manager_id INT);
insert into emp values (1, "Adam", "HR", "sqwdwe",4);
insert into emp values (2,"Bob","IT","referf",1);
insert into emp values (2,"Bob","IT","referf",3);
insert into emp values (2,"Bob","IT","referf",4);
insert into emp values (3,"Charlie","IT","ffefefv",1);
insert into emp values (3,"Charlie","IT","ffefefv",4);
insert into emp values (4,"Dale","Admin","ffev",3);
select * from emp;

select a.emp_id, a.emp_name, a.manager_id, b.emp_name from emp as a left join emp as b on a.manager_id=b.emp_id;

select emp_name from employees 












