SELECT
  "Date"            AS date,
  "Type_vehicule"   AS type_vehicule,
  "immat"           AS immat,
  "Score_Heure"     AS score_heure,
  "Vitesse"         AS vitesse,
  "Frein_brusques"  AS frein_brusques,
  "Acc_brusques"    AS acc_brusques,
  "Virages_brusques" AS virages_brusques,
  "Surregime"       AS surregime,
  "Total_points"    AS total_points,
  "Temps"           AS temps,
  "Distance"        AS distance,
  "conso"           AS conso
FROM {{ source('public', 'raw_conso') }}
