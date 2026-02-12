"""
Expected match outcome query. Home/Away/Draw.
Practice of case expressions.
"""

SELECT
  match_id,
  home_team_name,
  away_team_name,
  CASE
    WHEN home_goals_fulltime > away_goals_fulltime THEN 'Home Win'
    WHEN home_goals_fulltime < away_goals_fulltime THEN 'Away Win'
    ELSE 'Draw'
  END AS match_result
FROM football_data.matches;
