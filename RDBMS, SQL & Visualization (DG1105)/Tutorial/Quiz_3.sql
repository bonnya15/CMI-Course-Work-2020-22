create table tbl1(id int);

create table tbl2(id int);

insert into tbl1 values (1);
insert into tbl1 values (1);

insert into tbl2 values (1);
insert into tbl2 values (1);
insert into tbl2 values (1);


select * from tbl1;
select * from tbl2;


select tbl1.id, tbl2.id from tbl1 left outer join tbl2 on tbl1.id = tbl2.id;
select tbl1.id, tbl2.id from tbl1 right outer join tbl2 on tbl1.id = tbl2.id;
select tbl1.id, tbl2.id from tbl1 inner join tbl2 on tbl1.id = tbl2.id;

select tbl1.id, tbl2.id from tbl1 cross join tbl2;

select tbl1.id, tbl2.id from tbl1 left join tbl2 on tbl1.id = tbl2.id 
union all select tbl1.id, tbl2.id from tbl1 right outer join tbl2 on tbl1.id = tbl2.id;

select t1.id, t2.id from tbl2 as t1, t2;
select t1.id, t2.id from tbl1 t1 , tbl1 t2;

select t1.id, t2.id from tbl2 t1 , tbl2 t2;