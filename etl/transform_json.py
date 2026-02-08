import json
import pandas as pd
from pathlib import Path


def load_raw_json(file_path: str) -> dict:
    """
    Load raw match data from JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as json_data_file:
        return json.load(json_data_file)


def transform_matches(data: dict) -> pd.DataFrame:
    """
    Transform raw Football-Data.org JSON data to data suitable for BigQuery.
    """
    rows = []

    for match in data.get("matches", []):
        rows.append({
            "match_id": match.get("id"),
            "utc_date": match.get("utcDate"),
            "status": match.get("status"),
            "matchday": match.get("matchday"),
            "competition_code": match.get("competition", {}).get("code"),
            "competition_name": match.get("competition", {}).get("name"),
            "country": match.get("area", {}).get("name"),
            "home_team_id": match.get("homeTeam", {}).get("id"),
            "home_team_name": match.get("homeTeam", {}).get("name"),
            "away_team_id": match.get("awayTeam", {}).get("id"),
            "away_team_name": match.get("awayTeam", {}).get("name"),
            "home_goals": match.get("score", {}).get("fullTime", {}).get("home"),
            "away_goals": match.get("score", {}).get("fullTime", {}).get("away"),
            "last_updated": match.get("lastUpdated")
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    # Paths
    raw_data_path = "data/raw/pl_matches_25_26.json"
    output_path = "data/processed/matches_transformed.csv"

    # Load
    raw_data = load_raw_json(raw_data_path)

    # Transform
    df_matches = transform_matches(raw_data)

    # Save
    output_dir = Path(output_path).parent

    # Inspect
    print(df_matches.head())
    print(df_matches.tail())
    print(f"\nTotal matches transformed: {len(df_matches)}")
    print(f"Saved transformed data to {output_path}")
