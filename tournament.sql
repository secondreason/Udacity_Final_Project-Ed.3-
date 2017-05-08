-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players ( name VARCHAR(50),
                       id SERIAL PRIMARY KEY
);

CREATE TABLE matches ( win INT REFERENCES players(id),
                       loss INT REFERENCES players(id),
                       id SERIAL PRIMARY KEY
);

CREATE VIEW wins AS 
            select players.id, count(matches.win) as wins 
            from players left  join matches on players.id = matches.win 
            group by players.id;

CREATE VIEW matches_played AS
            select players.id, count(matches) as matches 
            from players left  join matches on players.id = matches.win or players.id = matches.loss 
            group by players.id;