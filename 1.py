with revenue as (select date_trunc('month',t.created_at)::date
    as month, sum(t.value) as revenue from 
    sf_transactions t
group by month
order by 1)

select

to_char(t.month,'YYYY-MM') as month,


round((t.revenue - lag(t.revenue) over (order by t.month))
* 100 / (lag(t.revenue) over (order by t.month)),2) as pct_change

from revenue t