# HungryPH: Manila Food Delivery Analytics

A modern data engineering pipeline simulating and analyzing food delivery patterns across Metro Manila.

## 🏗️ Architecture
- **Orchestration**: **Dagster** (using modern `Definitions` and `ConfigurableResource` patterns).
- **Ingestion (Bronze)**: Python-based simulation generating synthetic orders with realistic Manila traffic constraints.
- **Storage**: **PostgreSQL** running in **Docker**.
- **Transformation (Silver)**: **dbt** (Upcoming) for data cleaning, VAT calculations, and business logic.

## 🛠️ Project Structure
- `src/hungryph_analytics/defs/assets.py`: Data generation logic.
- `src/hungryph_analytics/defs/resources.py`: Database connection management.
- `src/hungryph_analytics/constant.py`: Manila-specific constants (cities, cuisines, rider speeds).

## 🚀 How to Run
1. **Clone the repo**:
   `git clone <your-repo-url>`
2. **Setup Environment**:
   - Copy `.env.example` to `.env` and fill in your details.
   - Run `uv sync` to install dependencies.
3. **Start Infrastructure**:
   `docker-compose up -d`
4. **Launch Pipeline**:
   `dg dev`

## 📊 The "Silver" Layer Plan
The next step is to implement dbt to:
1.  **Cleanse**: Standardize city names and filter out test data.
2.  **Enrich**: Calculate 12% VAT and delivery fees based on rider types.
3.  **Validate**: Ensure data integrity with dbt tests.
