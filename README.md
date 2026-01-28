# Sports Data Pipeline

A data engineering project that ingests football match data from a public API, processes and models the data using Python, and loads analytics ready tables into Google BigQuery for SQL based analysis.

This project demonstrates core data engineering skills including ETL/ELT design, data modeling, cloud data warehousing, and analytical SQL.

---

## Problem Statement

Raw sports data from public APIs is often unstructured and not optimized for analytics.  
The objective of this project is to design a reliable data pipeline that transforms raw football match data into a clean, queryable dataset that enables meaningful performance and trend based analysis.

---

## Architecture & Data Flow

**Source → Transform → Warehouse → Analytics**

1. **Data Source**
   - Public football API providing match level data in JSON format. (FOOTBALL-DATA.org free API)

2. **Ingestion**
   - Python scripts extract match data and store raw JSON files to preserve data lineage and replayability.

3. **Transformation**
   - Python is used to clean, normalize, and standardize match data.
   - Data is reshaped into structured, analytics-ready tables.

4. **Data Warehouse**
   - Transformed data is loaded into Google BigQuery.
   - Tables are optimized for analytical querying.

5. **Analytics Layer**
   - SQL queries are used to analyze team performance, match outcomes, and trends.

---

## Data Model

Primary analytics table (`football_data.matches`) includes:

- `match_id`
- `utc_date`
- `status`
- `matchday`
- `competition_code`
- `competition_name`
- `country`
- `home_team_name`
- `away_team_name`
- `home_goals`
- `away_goals`
- `last_updated`

This schema supports both match-level and team-level analysis.

---

## SQL Analytics

Analytical SQL queries are stored in the `sql/` directory.  
Each query answers a specific analytical question using BigQuery-compatible SQL.

---

### 📅 Premier League Matchday 1 Matches

**Objective:**  
Get all Premier League matches from matchday 1.

**Approach:**  
- Filter match data by competition code and matchday
- Return full match records for exploratory analysis

**Key SQL Concepts:**
- `WHERE` filtering
- Dataset-level querying

📸 **Query Output**

<img width="1100" height="350" alt="Image" src="https://github.com/user-attachments/assets/4bde3327-ddf0-41bf-a520-9b56865bc415" />

---

### ⚽ Total Goals Scored per Team

**Objective:**  
Calculate the total number of goals scored by each team across all matches.

**Approach:**  
- Aggregate goals scored when teams play at home and away
- Combine both perspectives into a single team-level dataset

**Key SQL Concepts:**
- Aggregations (`SUM`)
- `UNION ALL`
- Grouped analytics

📸 **Query Output**
<img width="1100" height="350" alt="Image" src="https://github.com/user-attachments/assets/c1692726-15f1-487a-be43-277b1c99c85d" />
---

### 🏆 Longest Winning Streak per Team

**Objective:**  
Identify the longest consecutive winning streak for each team.

**Approach:**  
- Combine home and away match results into a unified dataset
- Use window functions to segment win/loss data
- Arrange streaks to determine the longest winning run

**Key SQL Concepts:**
- Window functions (`SUM() OVER`)
- Conditional logic
- `UNION ALL`
- Analytical aggregation

📸 **Query Output**
<img width="1100" height="600" alt="Image" src="https://github.com/user-attachments/assets/9e038c71-4e01-4ac2-88e1-9a26bc90cb0b" />
---

## Technologies Used

- **Python** – Data ingestion, transformation, and pipeline logic
- **Google BigQuery** – Cloud data warehouse
- **SQL** – Analytical querying and reporting
- **Git / GitHub** – Version control and documentation

---

## Future Improvements

- Automate pipeline execution using cron or a workflow scheduler
- Implement incremental and partitioned loads in BigQuery
- Add data quality checks and logging
