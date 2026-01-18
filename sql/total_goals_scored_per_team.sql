"""
Calculates total goals scored by each team for both home and away goals
and returns them into a single row set.
"""

SELECT 
  home_team_name AS team,
  SUM(home_goals) AS goals_scored
FROM football_data.matches
GROUP BY team

UNION ALL

SELECT 
  away_team_name AS team,
  SUM(away_goals) AS goals_scored
FROM football_data.matches
GROUP BY team
