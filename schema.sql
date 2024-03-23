CREATE TABLE Team (
    team_id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    ranking INTEGER
);

CREATE TABLE Player (
    player_id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    team_id VARCHAR(100),
    num_test_matches INTEGER,
    num_t20_matches INTEGER,
    num_world_cup_matches INTEGER,
    num_odis INTEGER,
    player_type VARCHAR(100),
    statistics JSON,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);

CREATE TABLE Umpire (
    umpire_id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    country_of_origin VARCHAR(100),
    num_matches INTEGER
);

CREATE TABLE Coach (
    coach_id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    team_id VARCHAR(100),
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);

CREATE TABLE Captain (
    captain_id VARCHAR(100) PRIMARY KEY,
    player_id VARCHAR(100),
    num_years_captaincy INTEGER,
    num_wins INTEGER,
    FOREIGN KEY (player_id) REFERENCES Player(player_id) ON DELETE CASCADE
);

CREATE TABLE Match (
    match_id VARCHAR(100) PRIMARY KEY,
    stadium VARCHAR(100),
    winner_team_id VARCHAR(100),
    match_date DATE,
    match_time TIME,
    umpire_id VARCHAR(100),
    FOREIGN KEY (winner_team_id) REFERENCES Team(team_id) ON DELETE SET NULL,
    FOREIGN KEY (umpire_id) REFERENCES Umpire(umpire_id) ON DELETE SET NULL
);


CREATE OR REPLACE FUNCTION update_umpire_match_count() RETURNS TRIGGER AS $$
BEGIN
    UPDATE umpire SET num_matches = num_matches + 1 WHERE umpire_id = NEW.umpire_id;
    RETURN NEW;
END;


CREATE TRIGGER update_umpire_match_count
AFTER INSERT ON match
FOR EACH ROW EXECUTE FUNCTION update_umpire_match_count();