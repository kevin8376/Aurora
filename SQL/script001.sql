CREATE DATABASE IF NOT EXISTS AURORA;
USE AURORA;


-- game_stats table, will we used as a primary table
CREATE TABLE IF NOT EXISTS game_stats(
    PLAYER_NAME VARCHAR(30) PRIMARY KEY,
    PLAYER_LEVEL INT,
    SCORE INT DEFAULT 0,
    BADGES TEXT,
    PROGRESS VARCHAR(3) DEFAULT '0%'
                                       );

-- this table holds data for troops that player has unlocked
CREATE TABLE IF NOT EXISTS player_troops(
    PLAYER_NAME VARCHAR(30) NOT NULL UNIQUE,
    DELTA INT DEFAULT 1,
    TARDIS INT DEFAULT 0,
    BENZAMITE INT DEFAULT 0,
    MANDALORE INT DEFAULT 0,
    NEMESIS INT DEFAULT 0,
    ARMADA INT DEFAULT 0,
    ELSYIUM  INT DEFAULT 0,
    DEMOGORGON INT DEFAULT 0,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
                                         );

-- this table holds data for spells that player has unlocked
CREATE TABLE IF NOT EXISTS player_spells(
    PLAYER_NAME VARCHAR(30) NOT NULL UNIQUE,
    RAY_OF_SICKNESS INT DEFAULT 1,
    INCINERATE INT DEFAULT 0,
    PLASMA_DISCHARGE  INT DEFAULT 0,
    GOD_OF_CHAOS INT DEFAULT 0,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
                                         );

-- details of troops and spells attack defence and spells
CREATE TABLE IF NOT EXISTS spells(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    RAY_OF_SICKNESS INT DEFAULT 0,
    INCINERATE INT DEFAULT 0,
    PLASMA_DISCHARGE INT DEFAULT 0,
    GOD_OF_CHAOS INT DEFAULT 0,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS DELTA(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 10,
    DEFENCE INT DEFAULT 1,
    HEALTH INT DEFAULT 100,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS TARDIS(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 20,
    DEFENCE INT DEFAULT 2,
    HEALTH INT DEFAULT 200,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS BENZAMITE(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT  DEFAULT 40,
    DEFENCE INT DEFAULT 4,
    HEALTH INT DEFAULT 400,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS MANDALORE(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 60,
    DEFENCE INT  DEFAULT 6,
    HEALTH INT DEFAULT 600,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS NEMESIS(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 80,
    DEFENCE INT  DEFAULT 8,
    HEALTH INT DEFAULT 800,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS ARMADA(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 100,
    DEFENCE INT DEFAULT 10,
    HEALTH INT DEFAULT 1000,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS ELYSIUM(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 120,
    DEFENCE INT DEFAULT 12,
    HEALTH INT DEFAULT 1200,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

CREATE TABLE IF NOT EXISTS DEMOGORGON(
    PLAYER_NAME VARCHAR(30) UNIQUE,
    ATTACK INT DEFAULT 150,
    DEFENCE INT DEFAULT 15,
    HEALTH INT DEFAULT 1500,
    FOREIGN KEY (PLAYER_NAME) REFERENCES GAME_STATS(PLAYER_NAME)
);

COMMIT;