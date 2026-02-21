# 🛵 HungryPH: Manila Food Delivery Analytics

## 🏗️ Architecture
- **Ingestion**: Python simulation using **Dagster** generating orders for Makati, QC, Taguig, and Manila.
- **Storage**: **PostgreSQL** running in **Docker**.
- **Transformation**: **dbt** (Silver layer) for cleaning and VAT calculations.

## 🚀 How to Run
1. **Clone the repo**:
   `git clone <your-repo-url>`
2. **Setup Environment**:
   - Copy `.env.example` to `.env` and fill in your details.
   - Run `uv sync` (or `pip install -r requirements.txt`).
3. **Start Infrastructure**:
   `docker-compose up -d`
4. **Launch Pipeline**:
   `dg dev`