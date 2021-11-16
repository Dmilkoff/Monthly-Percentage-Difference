# Monthly-Percentage-Difference
Given a table of purchases by date, calculate the month-over-month percentage change in revenue. The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.
The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.

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
