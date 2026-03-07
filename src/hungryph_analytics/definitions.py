from dagster import Definitions, load_assets_from_modules
from .defs import assets, resources

from pathlib import Path
from dagster_dbt import load_assets_from_dbt_project

# Load assets from the assets module
python_assets = load_assets_from_modules([assets])

dbt_assets = load_assets_from_dbt_project(
    project_dir=Path(__file__).parent.parent.parent / "hungryph_dbt",
    dbt_resource=resources.dbt,
)

all_assets = python_assets + dbt_assets
# Define the Dagster definitions with assets and resources
defs = Definitions(
    assets=all_assets,
    resources={
        "db": resources.db,
        "dbt": resources.dbt,
    },
)
