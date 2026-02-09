import json
import pandas as pd
from pathlib import Path


def load_raw_json(file_path: Path) -> dict:
    """
    Load raw match data from JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as json_data_file:
        return json.load(json_data_file)


def transform_matches(data: dict) -> pd.DataFrame:
    """
    Transform raw Football-Data.org JSON data into a flat table.
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

            # Scores when finished
            "home_goals_fulltime": match.get("score", {}).get("fullTime", {}).get("home"),
            "away_goals_fulltime": match.get("score", {}).get("fullTime", {}).get("away"),

            # Extra data
            "last_updated": match.get("lastUpdated"),
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    # Project root (sports-data-pipeline/)
    BASE_DIR = Path(__file__).resolve().parent.parent

    raw_data_path = BASE_DIR / "data" / "raw" / "pl_matches_25_26.json"
    output_path = BASE_DIR / "data" / "processed" / "matches_transformed.csv"

    # Load
    raw_data = load_raw_json(raw_data_path)

    # Transform
    df_matches = transform_matches(raw_data)

    # Ensure output dir exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save
    df_matches.to_csv(output_path, index=False)

    # Inspect
    print("Transform successful ✅")
    print(df_matches[["status", "home_goals_fulltime", "away_goals_fulltime"]]
          .value_counts()
          .head(10))

    print(f"\nTotal matches transformed: {len(df_matches)}")
    print(f"Saved transformed data to: {output_path}")
