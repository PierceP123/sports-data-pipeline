from google.cloud import bigquery

def load_to_bigquery(df):
    client = bigquery.Client()

    bigquery_table_id = "sports-data-pipeline-484205.football_data.matches"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"
    )

    job = client.load_table(
        df,
        bigquery_table_id,
        job_config=job_config
    )

    job.result()
