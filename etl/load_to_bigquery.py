from google.cloud import bigquery
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Service account JSON path from .env
SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not SERVICE_ACCOUNT_JSON:
    raise ValueError("Please set GOOGLE_APPLICATION_CREDENTIALS in your .env file")

# Project and table
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "sports-data-pipeline-484205")
TABLE_ID = os.getenv("BIGQUERY_TABLE", "football_data.matches")  # dataset.table

def load_to_bigquery():
    # Project root
    BASE_DIR = Path(__file__).resolve().parent.parent

    csv_path = BASE_DIR / "data" / "processed" / "matches_transformed.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows from CSV")

    # Connect to BigQuery using service account
    client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON, project=PROJECT_ID)

    # Full table ID
    full_table_id = f"{PROJECT_ID}.{TABLE_ID}"

    # Load config
    job_config = bigquery.LoadJobConfig(write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE)

    # Load dataframe
    job = client.load_table_from_dataframe(df, full_table_id, job_config=job_config)
    job.result()

    print(f"Table fully refreshed: {full_table_id}")
    print(f"Rows in table now: {client.get_table(full_table_id).num_rows}")

if __name__ == "__main__":
    load_to_bigquery()
