-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- Delete database if already existed.
-- Tables and views deletion is unecessary since the whole database is deleted.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to tournament database
\c tournament;

CREATE TABLE players(
	id SERIAL PRIMARY KEY, 
	name TEXT);
CREATE TABLE matches(
	winner INTEGER REFERENCES players(id), 
	loser INTEGER REFERENCES players(id), 
	PRIMARY KEY(winner, loser));

CREATE VIEW player_ranking AS(
SELECT players.id as player_id, players.name,
COUNT(matches.winner) AS wins,
COUNT(matches.*) AS total_matches
FROM players LEFT JOIN matches ON players.id=matches.winner OR players.id=matches.loser
GROUP BY players.id
ORDER BY wins DESC, total_matches DESC
);
