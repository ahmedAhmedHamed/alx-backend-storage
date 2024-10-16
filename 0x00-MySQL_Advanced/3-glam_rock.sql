-- bands with Glam rock as their main style, ranked by their longevity
-- bands with Glam rock as their main style, ranked by their longevity
select band_name, IFNULL(split, 2022) - formed as lifespan
from metal_bands
where LOCATE('Glam Rock',style) != 0;

