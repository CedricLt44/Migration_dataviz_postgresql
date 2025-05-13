-- Ce fichier utilise les modèles de staging
SELECT 
    i.type_vehicule,
    ROUND(SUM(e.cost)::numeric, 2) AS total_cost,
    ROUND(AVG(c.conso)::numeric,2) AS avg_conso,
    ROUND(SUM(c.distance)::numeric,0) AS total_distance
    
FROM {{ ref('stg_raw_entretiens') }} e
JOIN {{ ref('stg_raw_immat') }} i
  ON e.immat = i.immat
JOIN {{ ref('stg_raw_conso') }} c
  ON e.immat = c.immat

GROUP BY i.type_vehicule