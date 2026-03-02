with orders as (
    select * from {{ ref('stg_orders') }}
),

calculated as (
    select
        *,
        -- 12% VAT calculation
        round(cast(amount_php * 0.12 as numeric), 2) as vat_amount,
        
        -- Delivery fee based on rider type
        case 
            when rider_type = 'Bicycle' then 49
            when rider_type = 'Motorcycle' then 59
            when rider_type = 'Car' then 89
            else 0 
        end as delivery_fee
    from orders
),

final as (
    select
        *,
        -- Total amount including delivery fee
        (amount_php + delivery_fee) as total_amount_paid,
        -- Net amount excluding VAT
        (amount_php - vat_amount) as net_amount
    from calculated
)

select * from final
