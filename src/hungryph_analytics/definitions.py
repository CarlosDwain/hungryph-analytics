from dagster import Definitions, load_assets_from_modules
from .defs import assets, resources

# Load assets from the assets module
all_assets = load_assets_from_modules([assets])

# Define the Dagster definitions with assets and resources
defs = Definitions(
    assets=all_assets,
    resources={
        "db": resources.db,
    },
)
