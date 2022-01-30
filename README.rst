Test Sql

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
