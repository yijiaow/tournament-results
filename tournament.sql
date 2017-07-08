-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
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

CREATE OR REPLACE VIEW matches_won AS(
SELECT players.id AS id, players.name AS name,
COUNT (matches.winner) AS wins
FROM players LEFT JOIN matches
ON players.id = matches.winner
GROUP BY players.id);

CREATE OR REPLACE VIEW matches_total AS(
SELECT players.id AS id, COUNT(matches.*) AS total
FROM players LEFT JOIN matches
ON players.id=matches.winner OR players.id=matches.loser
GROUP BY players.id);

CREATE OR REPLACE VIEW standings AS(
SELECT matches_won.id, matches_won.name, matches_won.wins, matches_total.total
FROM matches_won RIGHT JOIN matches_total
ON matches_won.id=matches_total.id
ORDER BY matches_won.wins DESC, matches_total.total DESC);