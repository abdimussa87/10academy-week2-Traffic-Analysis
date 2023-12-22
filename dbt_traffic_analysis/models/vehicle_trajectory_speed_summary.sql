WITH trajectory_speed_summary AS (
    SELECT
        *
    FROM {{ ref('trajectory_speed_summary') }}
    WHERE avg_speed_recorded_for_track > 50
)

SELECT 
    * 
FROM
    vehicle_information
Join trajectory_speed_summary
USING(track_id)