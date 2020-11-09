DROP TABLE tournaments;
DROP TABLE players;
DROP TABLE games;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    number INT
);

CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    player1_id INT REFERENCES players(id) ON DELETE CASCADE,
    player2_id INT REFERENCES players(id) ON DELETE CASCADE,
    game_id INT REFERENCES games(id) ON DELETE CASCADE,
    winner VARCHAR(255),
    loser VARCHAR(255)
)