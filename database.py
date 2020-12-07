from tkinter import *
import sqlite3

connection=sqlite3.connect("data.db")
cursor=connection.cursor()
#cursor.execute("CREATE TABLE plays(game_number INT          NOT NULL, p1name      VARCHAR(255) NOT NULL, p1score     FLOAT        NOT NULL, p2name      VARCHAR(255) NOT NULL, p2score     FLOAT        NOT NULL  )")
cursor.execute("INSERT INTO plays VALUES(1, 'Elliot', 0, 'Brendan', 1),(2, 'Bob', 1, 'Brendan', 0),(3, 'Bob', 1, 'Elliot', 0),(4, 'Jane', 1, 'Bob', 0),(5, 'Bob', 0, 'Brendan', 1),(6, 'Jane', 1, 'Elliot', 0)")
x= cursor.execute( "WITH RECURSIVE p(current_game_number)
                   AS( WITH players AS(SELECT DISTINCT p1name AS player_name FROM plays UNION SELECT DISTINCT p2name FROM plays) SELECT 0   AS game_number,player_name, 1000.0 FLOAT AS previous_elo,1000.0 FLOAT AS new_elo FROM players UNION ALL( WITH previous_elos AS (SELECT * FROM p)SELECT plays.game_number, player_name, previous_elos.new_elo AS previous_elo, round(CASE WHEN player_name NOT IN (p1name, p2name) THEN previous_elos.new_elo  WHEN player_name = p1name  THEN previous_elos.new_elo + 32.0 * (p1score - (r1 / (r1 + r2))) ELSE previous_elos.new_elo + 32.0 * (p2score - (r2 / (r1 + r2))) END) FROM plays JOIN previous_elos  ON current_game_number = plays.game_number - 1 JOIN LATERAL (   SELECT    pow(10.0, (SELECT new_elo               FROM previous_elos               WHERE current_game_number = plays.game_number - 1 AND player_name = p1name) / 400.0) AS r1,    pow(10.0, (SELECT new_elo FROM previous_elos   WHERE current_game_number = plays.game_number - 1 AND player_name = p2name) / 400.0) AS r2  ) r ON TRUE )SELECT  player_name,  (    SELECT new_elo    FROM p   WHERE t.player_name = p.player_name    ORDER BY current_game_number DESC    LIMIT 1  )                    AS elo,  count(CASE WHEN previous_elo < new_elo    THEN 1        ELSE NULL END) AS wins,  count(CASE WHEN previous_elo > new_elo    THEN 1        ELSE NULL END) AS losses FROM  (    SELECT *    FROM p    WHERE previous_elo <> new_elo    ORDER BY current_game_number, player_name  ) t     GROUP BY player_name   ORDER BY elo DESC")
print(x)
cursor.close()
connection.close()
