import os
import pandas as pd
import random
import uuid
import dagster as dg
from .resources import PostgresResource
from hungryph_analytics.constant import CITIES, FOOD_TYPES, PAYMENT_METHODS, RIDER_TYPES, RIDER_CONFIG

@dg.asset
def raw_orders(db: PostgresResource):
    orders = []
    for _ in range(100):
        city_name = random.choice(list(CITIES.keys()))
        coords = CITIES[city_name]
        rider = random.choice(RIDER_TYPES)
        base_speed = RIDER_CONFIG[rider]["avg_speed"]
        
        # Add some random traffic variance (-5 to +5 km/h)
        actual_speed = max(5, base_speed + random.uniform(-5, 5))
        
        orders.append({
            "order_id": str(uuid.uuid4()),
            "city": city_name,
            "latitude": coords["lat"] + random.uniform(-0.01, 0.01),
            "longitude": coords["lon"] + random.uniform(-0.01, 0.01),
            "cuisine": random.choice(FOOD_TYPES),
            "amount_php": round(random.uniform(150, 2000), 2),
            "payment_method": random.choice(PAYMENT_METHODS),
            "rider_type": rider,
            "avg_speed_kmh": round(actual_speed, 2),
            "timestamp": pd.Timestamp.now()
        })
    
    df = pd.DataFrame(orders)
    
    engine = db.get_engine()
    
    # Send to Postgres, if_exists='append' to add to existing data, 'replace' to overwrite
    df.to_sql("hungryph_orders", engine, if_exists="append", index=False)
    
    return dg.MaterializeResult(
        metadata={
            "row_count": len(df),
            "motorcycle_ratio": len(df[df['rider_type'] == 'Motorcycle']) / len(df) if len(df) > 0 else 0
        }
    )