from extract_api_to_json import extract_api_to_json
from transform_json import transform_json
from load_to_bigquery import load_to_bigquery

def main():
    raw_data = extract_api_to_json()
    df = transform_json(raw_data)
    load_to_bigquery(df)

if __name__ == "__main__":
    main()
