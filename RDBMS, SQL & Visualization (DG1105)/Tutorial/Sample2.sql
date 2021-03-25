create table sample2 (
						roll_num int,
                        s_name varchar(20),
                        grade varchar(2),
                        p_money int);
                        
insert into sample2
vaLues('01','Prasun','AB','5000');
insert into sample2 values ('02' , 'Shiuli' , 'A','4500');
insert into sample2 values ('03' , 'Megha' , 'A','3500');
insert into sample2 values ('03' , 'Megha' , 'A','3500');
select * from sample2;
select distinct * from sample2;
create table sample3 as (select distinct * from sample2);
select s_name as student from sample3 where p_money > 4500;
drop table sample2 ;
alter table sample3
rename to sample1;
select * from sample1 as A, sample1 as B; 
select * from sample1 as A, sample1 as B
where A.p_money > B.p_money; 
select A.s_name as Higher, B.s_name as lower from sample1 as A, sample1 as B 
where A.p_money > B.p_money;