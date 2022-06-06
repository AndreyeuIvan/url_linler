Task

Python: 
1. Create a registration page (Using Bootstrap)
2. Create a login page (Django + Allauth)
3. Create a link shortening page (using Bootstrap)
4. Create a separate page with the history of saved links (Added Postgres for saving inputed urls)

Sql

1 Task:
  SELECT * client_number, COUNT(CASE WHEN outcome='win' THEN 'win' END) AS WIN, COUNT(CASE WHEN outcome='lose' THEN 'lose' END) AS LOSE 
  FROM bid 
  LEFT JOIN event_value
  ON bid.play_id = event_value.play_id
  GROUP BY client_number;

2 Task
  SELECT game, count(*) as games_count
  FROM (SELECT CONCAT(least(away_team, home_team), '-', greatest(away_team,home_team)) 
  AS game
  FROM event_entity) as a
  GROUP BY game 
  ORDER BY games_count;
