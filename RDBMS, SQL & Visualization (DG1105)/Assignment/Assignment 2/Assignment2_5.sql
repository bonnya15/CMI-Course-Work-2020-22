-- Question 5
select symbol, Dates, LowPrice from stock where Dates between '2018-12-03' and '2018-12-07';
select symbol, Dates , HighPrice from stock where Dates between '2018-12-24' and '2018-12-31';


select c.symbol, c.Dates, c.LowPrice,p.symbol, p.dates, p.HighPrice , (p.HighPrice - c.LowPrice)/c.LowPrice*100 as percentage
from (select * from stock where Dates between '2018-12-03' and '2018-12-07') as c
inner join (select * from stock where Dates between '2018-12-24' and '2018-12-31') as p on c.symbol = p.symbol;


select * from (select c.symbol, c.Dates as InvestmentDate, c.LowPrice, p.dates as WithdrawalDate, p.HighPrice , (p.HighPrice - c.LowPrice)/c.LowPrice*100 as percentage
from (select * from stock where Dates between '2018-12-03' and '2018-12-07') as c
inner join (select * from stock where Dates between '2018-12-24' and '2018-12-31') as p on c.symbol = p.symbol) as der 
order by der.percentage desc limit 1;

select (5000 - 5000 % der.LowPrice) / der.LowPrice as num_stock  from (select c.symbol, c.Dates as InvestmentDate, c.LowPrice, p.dates as WithdrawalDate, p.HighPrice , (p.HighPrice - c.LowPrice)/c.LowPrice*100 as percentage
from (select * from stock where Dates between '2018-12-03' and '2018-12-07') as c
inner join (select * from stock where Dates between '2018-12-24' and '2018-12-31') as p on c.symbol = p.symbol) as der 
order by der.percentage desc limit 1;
 
select der.symbol, (5000 - 5000 % der.LowPrice) / der.LowPrice as num_stock, 
(5000 - 5000 % der.LowPrice) / der.LowPrice * (der.HighPrice - der.LowPrice) as Profit
from (select c.symbol, c.Dates as InvestmentDate, c.LowPrice, p.dates as WithdrawalDate, p.HighPrice , (p.HighPrice - c.LowPrice)/c.LowPrice*100 as percentage
from (select * from stock where Dates between '2018-12-03' and '2018-12-07') as c
inner join (select * from stock where Dates between '2018-12-24' and '2018-12-31') as p on c.symbol = p.symbol) as der 
order by der.percentage desc limit 1;
  
 
 