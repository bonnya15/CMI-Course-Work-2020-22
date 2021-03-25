create table results(
playerID varchar(20),
tournamentID varchar(20),
gameID varchar(20),
color int, 
result int);
insert into results values('p1','t1','g1', 1 , 1);
insert into results values('p2','t1','g1', 2 , -1);
insert into results values('p3','t1','g2', 1 , 0);
insert into results values('p4','t1','g2', 2 , 0);
insert into results values('p1','t1','g3', 1 , 1);
insert into results values('p3','t1','g3', 2 , -1);
insert into results values('p2','t1','g4', 1 , -1);
insert into results values('p4','t1','g4', 2 , 1);
insert into results values('p2','t1','g5', 1 , 0);
insert into results values('p3','t1','g5', 2 , 0);
insert into results values('p1','t2','g6', 1 , 0);
insert into results values('p2','t2','g6', 2 , 0);
insert into results values('p3','t2','g7', 1 , -1);
insert into results values('p4','t2','g7', 2 , 1);
insert into results values('p1','t2','g8', 1 , 1);
insert into results values('p3','t2','g8', 2 , -1);
insert into results values('p2','t2','g9', 1 , 1);
insert into results values('p4','t2','g9', 2 , -1);
insert into results values('p2','t2','g10', 1 , 0);
insert into results values('p3','t2','g10', 2 , 0);

select * from results;
select count(*) from results group by playerID;
select playerID, count(result) as m from results where (result = 1) group by playerID; 
-- select playerID , min(t) from (select playerID, count(result) as t from results where result = 1 group by playerID) new;
-- select playerID , min(t) from ((select playerID, count(result) as t from results where result = 1 group by playerID) as a
-- inner join min(t) as b on t = min(t));
