create table employee(
EmpCode int not null, 
EmpFName varchar(20), 
EmpLName varchar(20), 
Job varchar(20),
Manager int, 
HireDate date, 
Salary int, 
Commission int, 
DeptCode int);
insert into employee values(9369, 'TONY', 'STARK', 'SOFTWARE ENGINEER', 7902, '1980-12-17', 2800,0,20);
insert into employee values(9499, 'TIM', 'ADOLF', 'SALESMAN', 7698, '1981-02-20', 1600, 300,30  );
insert into employee values(9566, 'KIM', 'JARVIS', 'MANAGER', 7839, '1981-04-02', 3570,0,20);
insert into employee values(9566, 'K', 'J', 'MANAGER', 7839, '1981-04-02', 2800,0,20);
select EmpFname, emplName from employee;
select concat(EmpFname,' ', empLname) as Name, commission
from employee 
where commission > 0
and job != 'Analyst';
select * from employee where job = binary'SALESMAN';
select * from employee where Salary>2000 and (job = 'MANAGER' or Commission > 0);