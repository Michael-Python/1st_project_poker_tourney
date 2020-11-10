DROP TABLE tournaments;
DROP TABLE games;
DROP TABLE players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1 INT REFERENCES players(id) ON DELETE CASCADE,
    player2 INT REFERENCES players(id) ON DELETE CASCADE,
    number INT
);

CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    game_id INT REFERENCES games(id) ON DELETE CASCADE,
    winner INT REFERENCES players(id) ON DELETE CASCADE,
    loser INT REFERENCES players(id) ON DELETE CASCADE
)