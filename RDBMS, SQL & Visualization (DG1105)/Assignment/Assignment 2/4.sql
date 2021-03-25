-- Question 4

select
((select count(distinct dates) from stock)
- (select count(distinct dates) from stock
where PrevClose>ClosePrice)) as "All Five stocks closed higher",
((select count(distinct dates) from stock)
- (select count(distinct dates) from stock
where PrevClose<ClosePrice)) as "All Five stocks closed Lower" ;

select Dates from stock where ClosePrice > PrevClose group by Dates having count(Symbol)=5;
select Dates from stock where ClosePrice < PrevClose group by Dates having count(Symbol)=5;