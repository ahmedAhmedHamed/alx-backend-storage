-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- using aggregated query
select origin, sum(fans) as nb_fans
from metal_bands
GROUP BY origin
order by nb_fans desc
LIMIT 9;

