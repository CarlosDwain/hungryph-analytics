from dagster import Definitions, load_assets_from_modules, AssetExecutionContext
from .defs import assets, resources

from pathlib import Path
from dagster_dbt import DbtCliResource, dbt_assets, DbtProject

dbt_project_dir = Path(__file__).parent.parent.parent / "hungryph_dbt"
dbt_project = DbtProject(project_dir=dbt_project_dir)

dbt_project.prepare_if_dev()

@dbt_assets(manifest=dbt_project.manifest_path)
def hungryph_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource): yield from dbt.cli(["build"], context=context).stream()

# Load assets from the assets module
python_assets = load_assets_from_modules([assets])

all_assets = python_assets + [hungryph_dbt_assets]
# Define the Dagster definitions with assets and resources
defs = Definitions(
    assets=all_assets,
    resources={
        "db": resources.db,
        "dbt": resources.dbt,
    },
)
