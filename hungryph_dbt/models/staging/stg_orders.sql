with source as (
    select * from {{ source('raw_data', 'hungryph_orders') }}
),

renamed as (
    select
        order_id,
        city,
        latitude,
        longitude,
        cuisine,
        amount_php,
        payment_method,
        rider_type,
        avg_speed_kmh,
        timestamp as ordered_at
    from source
)

select * from renamed
