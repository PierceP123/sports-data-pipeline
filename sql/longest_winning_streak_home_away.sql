"""
Calculates the longest winning streak for each team by combining home and away matches,
tracking consecutive wins over time and returning the maximum win streak per team.
"""

WITH all_matches AS (
    SELECT
        home_team_name AS team,
        utc_date,
        CASE 
            WHEN home_goals > away_goals THEN 1
            ELSE 0
        END AS win
    FROM football_data.matches

    UNION ALL

    SELECT
        away_team_name AS team,
        utc_date,
        CASE 
            WHEN away_goals > home_goals THEN 1
            ELSE 0
        END AS win
    FROM football_data.matches
),

winning_streak AS (
    SELECT
        team,
        utc_date,
        win,
        SUM(CASE WHEN win = 0 THEN 1 ELSE 0 END) OVER (
            PARTITION BY team
            ORDER BY utc_date
        ) AS streak_group
    FROM all_matches
),

games_in_a_row AS (
    SELECT
        team,
        streak_group,
        COUNTIF(win = 1) AS consecutive_wins
    FROM winning_streak
    GROUP BY team, streak_group
)

SELECT
    team,
    MAX(consecutive_wins) AS longest_win_streak
FROM games_in_a_row
GROUP BY team
ORDER BY longest_win_streak DESC;
