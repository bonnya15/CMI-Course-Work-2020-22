-- Question 1
create database assignment;
select * from stock;
select count(*) from stock;

-- Question 2
select b.Symbol as Symbol , b.max - a.ClosePrice as Max_Gain , -b.min + a.ClosePrice as Max_Loss from(
(select ClosePrice from stock where symbol = 'APOLLOHOSP' and Dates = '2017-11-02') as a,
(select symbol, max(ClosePrice) as max , min(ClosePrice) as min from stock where symbol = 'APOLLOHOSP') as b
) union
select b.Symbol as Symbol , b.max - a.ClosePrice as Max_Gain , -b.min + a.ClosePrice as Max_Loss from(
(select ClosePrice from stock where symbol = 'ICICIBANK' and Dates = '2017-11-02') as a,
(select symbol, max(ClosePrice) as max , min(ClosePrice) as min from stock where symbol = 'ICICIBANK') as b
) union
select b.Symbol as Symbol , b.max - a.ClosePrice as Max_Gain , -b.min + a.ClosePrice as Max_Loss from(
(select ClosePrice from stock where symbol = 'INDIGO' and Dates = '2017-11-02') as a,
(select symbol, max(ClosePrice) as max , min(ClosePrice) as min from stock where symbol = 'INDIGO') as b
) union
select b.Symbol as Symbol , b.max - a.ClosePrice as Max_Gain , -b.min + a.ClosePrice as Max_Loss from(
(select ClosePrice from stock where symbol = 'RELIANCE' and Dates = '2017-11-02') as a,
(select symbol, max(ClosePrice) as max , min(ClosePrice) as min from stock where symbol = 'RELIANCE') as b
) union
select b.Symbol as Symbol , b.max - a.ClosePrice as Max_Gain , -b.min + a.ClosePrice as Max_Loss  from(
(select ClosePrice from stock where symbol = 'SUNTV' and Dates = '2017-11-02') as a,
(select symbol, max(ClosePrice) as max , min(ClosePrice) as min from stock where symbol = 'SUNTV') as b
);

select Symbol, max(d) as Maximum_Gain, -min(d) as Maximum_Loss from 
(select Symbol, (ClosePrice-a) as d from stock,(select Symbol as n, ClosePrice as a from stock where Dates="2017-11-02") as b 
where Symbol=n) as c
group by Symbol;

-- Question 3
-- select symbol, (ClosePrice - PrevClose)/PrevClose * 100 as gain from stock where (ClosePrice - PrevClose)/PrevClose * 100 > 3;

select symbol, count(symbol) as gain from stock where (ClosePrice - PrevClose)/PrevClose * 100 > 3 group by symbol;



