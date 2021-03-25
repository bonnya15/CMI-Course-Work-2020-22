show tables;
create table course(course_id varchar(20), title varchar(20), dept_name varchar(20), credits INT);

insert into course values ('BIO-301', 'Genetics', 'Biology', 4);
insert into course values ('CS-190', 'Game Design', 'Comp Sc', 4);
insert into course values ('CS-315', 'Robotics', 'Comp Sc', 2);


create table prereq (course_id varchar(20), prereq_id varchar(20));

insert into prereq values ('BIO-301', 'BIO-101');
insert into prereq values ('CS-190', 'CS-101');
insert into prereq values ('CS-347', 'CS-101');




create table customer(customer_id INT, customer_name varchar(30), city varchar(20), grade INT, salesman_id INT);
insert into customer values(3002,'Nick Rimando','New York',100,5001);
insert into customer values(3007,'Brad Davis','New York',200,5001);
insert into customer values(3005,'Graham Zusi','California',200,5002);
insert into customer values(3008,'Julian Green','London',300,5002);
insert into customer values(3004,'Fabian Johnson','Paris',300,5006);
insert into customer values(3009,'Geoff Cameron','Berlin',100,5003);
insert into customer values(3003,'Jozy Altidor','Moscow',200,5007);
insert into customer values(3001,'Brad Guzan','London', Null ,5005);






create table salesman(salesman_id int, name varchar(30), city varchar(20), commission float);

insert into salesman values (5001, 'James Hoog', 'New York', 0.15);
insert into salesman values (5002, 'Nail Knite', 'Paris', 0.13);
insert into salesman values (5005, 'Pit Alex', 'London', 0.11);
insert into salesman values (5006, 'Mc Lyon', 'Paris', 0.14);
insert into salesman values (5007, 'Paul Adam', 'Rome', 0.13);
insert into salesman values (5003, 'Lauson Hen', 'San Jose', 0.12);

select * from salesman where commission > 0.12;
select * from salesman where city = 'Paris';
select * from salesman;
select min(commission) from salesman;
select sum(commission) from salesman;
select * from salesman where commission = (select min(commission) from salesman)LIMIT 0,1000;
select * from salesman order by salesman_id limit 3,1 ; -- After the 3 values we are taking one from the next values

-- Inner joins and Outer Joins 
-- Inner join does intersection of two sets 

select * from course;
select * from prereq;

-- Natural Join takes all the possible columns
select * from course inner join prereq;
select * from course inner join prereq on course.course_id = prereq.course_id;
-- In this case loss of data is there. 

select c.course_id, p.prereq_id, c.title, c.dept_name, c.credits from course as c left outer join prereq as p on  c.course_id = p.course_id;
select p.course_id, p.prereq_id, c.title, c.dept_name, c.credits from course as c right outer join prereq as p on  c.course_id = p.course_id;
select p.course_id, p.prereq_id, c.title, c.dept_name, c.credits from course as c right outer join prereq as p using(course_id);

select * from course left join prereq using(course_id) union select * from course right join prereq as p using(course_id);

select c.course_id, p.prereq_id, c.title, c.dept_name, c.credits from course as c left join prereq as p using(course_id) union select p.course_id, p.prereq_id, c.title, c.dept_name, c.credits from course as c right join prereq as p using(course_id);

select * from course 
natural join prereq; 

select * from course 
cross join prereq;  -- Cartesian product

select * from salesman;
select * from customer;
select * from customer inner join salesman using(salesman_id);

select * from customer natural join salesman;

-- select * from customer left join salesman using(customer_id, 

select a.customer_id as 'ID', a.customer_name as 'C.name' , a.grade, b.name as 'S.name' , a.city, b.commission from customer a
left outer join salesman b
on a.salesman_id = b.salesman_id
where a.grade < 300
order by ID;


select * from customer right outer join salesman using(salesman_id);
select * from customer left outer join salesman using(salesman_id);