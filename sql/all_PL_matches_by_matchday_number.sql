""" 
Query to select all matches in the Premier League from any matchday.
Showing results from each game. Matchday number can be changed to suit.
"""

SELECT *
FROM football_data.matches
WHERE competition_code = 'PL' AND matchday = 1;