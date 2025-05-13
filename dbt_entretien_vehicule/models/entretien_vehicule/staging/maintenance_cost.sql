SELECT r.immat, SUM(e.cost) AS Total_cost, r.type_vehicule
FROM {{ source('public', 'raw_entretiens') }} e
JOIN {{ source('public', 'raw_immat') }} r
  ON e.immat = r.immat
GROUP BY r.immat, r.type_vehicule;
