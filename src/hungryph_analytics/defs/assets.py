import os
import pandas as pd
import random
import uuid
import dagster as dg # The new standard way to import
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Keeping your local PH constants
from hungryph_analytics.constant import CITIES, FOOD_TYPES, PAYMENT_METHODS

load_dotenv()

# Database setup
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)

@dg.asset
def raw_orders():
    """
    Bronze Layer: Simulates 100 orders from Metro Manila.
    Using @dg.asset tells Dagster this is a modern component-managed asset.
    """
    orders = []
    for _ in range(100):
        city_name = random.choice(list(CITIES.keys()))
        coords = CITIES[city_name]
        orders.append({
            "order_id": str(uuid.uuid4()),
            "city": city_name,
            "latitude": coords["lat"] + random.uniform(-0.01, 0.01),
            "longitude": coords["lon"] + random.uniform(-0.01, 0.01),
            "cuisine": random.choice(FOOD_TYPES),
            "amount_php": round(random.uniform(150, 2000), 2),
            "payment_method": random.choice(PAYMENT_METHODS),
            "timestamp": pd.Timestamp.now()
        })
    
    df = pd.DataFrame(orders)
    
    # Send to Postgres
    df.to_sql("bronze_orders", engine, if_exists="append", index=False)
    
    return dg.MaterializeResult(
        metadata={
            "num_records": len(df),
            "preview": dg.MetadataValue.md(df.head().to_markdown())
        }
    )