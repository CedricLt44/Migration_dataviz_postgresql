WITH stg_raw_immat AS (
    SELECT * FROM {{ ref('stg_raw_immat') }}
),
stg_raw_entretiens AS (
    SELECT * FROM {{ ref('stg_raw_entretiens') }}
),
-- Standardisation et comptage des opérations
operations_count AS (
    SELECT 
        v.type_vehicule,
        -- Standardiser le texte de l'opération
        UPPER(TRIM(m.operation)) AS operation,
        COUNT(*) AS operation_count
    FROM stg_raw_immat v
    JOIN stg_raw_entretiens m
        ON m.immat = v.immat
    GROUP BY v.type_vehicule, UPPER(TRIM(m.operation))
),
-- Consolidation des opérations
operations_consolidated AS (
    SELECT
        type_vehicule,
        operation,
        SUM(operation_count) AS operation_count
    FROM operations_count
    GROUP BY type_vehicule, operation
),
-- Calcul du total des opérations
total_operations AS (
    SELECT
        type_vehicule,
        SUM(operation_count) AS total_operation_count
    FROM operations_consolidated
    GROUP BY type_vehicule
)
-- Résultat final
SELECT 
    o.type_vehicule,
    o.operation,
    o.operation_count,
    t.total_operation_count,
    ROUND((o.operation_count::numeric / t.total_operation_count) * 100, 2) AS operation_percentage
FROM operations_consolidated o
JOIN total_operations t
  ON o.type_vehicule = t.type_vehicule
ORDER BY o.type_vehicule, o.operation