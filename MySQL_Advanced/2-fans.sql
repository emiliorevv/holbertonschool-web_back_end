-- Select the origin and sum of fans for each origin, ordering by the number of fans in descending order
SELECT origin, SUM(fans) as nb_fans FROM metal_bands GROUP BY origin
ORDER BY nb_fans DESC;