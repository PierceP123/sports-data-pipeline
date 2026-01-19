"""
Summary of total goals and average goal per match for each matchday.
Showing trend analysis from dataset.
"""

SELECT
  matchday,
  SUM(home_goals + away_goals) AS total_goals,
  ROUND(AVG(home_goals + away_goals)) AS avg_goals_per_match
FROM football_data.matches
GROUP BY matchday
ORDER BY matchday;