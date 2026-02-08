from extract_api_to_json import extract_data
from transform_json import transform_data
from load_to_bigquery import load_to_bigquery

def main():
    raw_data = extract_data()
    df = transform_data(raw_data)
    load_to_bigquery(df)

if __name__ == "__main__":
    main()
