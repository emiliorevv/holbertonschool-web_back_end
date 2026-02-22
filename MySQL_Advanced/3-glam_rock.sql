-- Select the band name and lifespan, ordering by the lifespan in descending order
SELECT
    band_name,
    (CASE
        WHEN split IS NULL THEN 2024
        ELSE split
     END - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;