from dagster import ConfigurableResource, EnvVar
from sqlalchemy import create_engine, Engine

class PostgresResource(ConfigurableResource):
    user: str
    password: str
    host: str
    port: str
    database: str
    
    def get_engine(self) -> Engine:
        url=f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        return create_engine(url)
    
db = PostgresResource(
    user=EnvVar("DB_USER"),
    password=EnvVar("DB_PASSWORD"),
    host=EnvVar("DB_HOST"),
    port=EnvVar("DB_PORT"),
    database=EnvVar("DB_NAME"),
)