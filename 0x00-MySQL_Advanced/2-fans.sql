-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- using an uncorrelated subquery
select m1.origin, m1.fans
from metal_bands m1
JOIN (
  select origin, MAX(fans) AS fans
  from metal_bands
  GROUP BY origin) as m2
  ON m1.origin = m2.origin and m1.fans = m2.fans;
  
