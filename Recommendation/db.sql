CREATE DATABASE TwitchRecommend;
CREATE TABLE 'TwitchRecommend'.'login' (
	'user_id' BIGINT AUTO_INCREMENT,
	'user_name' VARCHAR(45) NULL,
	'user_password' VARCHAR(100) NULL,
	PRIMARY KEY ('user_id'));

DELIMITER $$
CREATE DEFINER='root'@'localhost' PROCEDURE 'getGameNameFromDB'(
	IN p_user_id VARCHAR(20)
)
BEGIN
	select * from login where user_id = p_user_id;
END$$
DELIMITER;

CREATE TABLE 'TwitchRecommend'.'userLikedTags'(
	'user_id' BIGINT,
	'game_name' VARCHAR(45) NULL,
	'game_id' VARCHAR(45) NULL,
	FOREIGN KEY(user_id)
	REFERENCES login(user_id)
);


CREATE TABLE 'TwitchRecommend'.'data'(
	'game_id' VARCHAR(45) NULL,
	'url' VARCHAR(100) NULL,
	'ts' TIMESTAMP NULL
	PRIMARY KEY ('game_id')	
);

DELIMITER $$
CREATE DEFINER='root'@'localhost' PROCEDURE 'getGameClips'(
	IN p_game_name VARCHAR(20), 
	IN p_game_id VARCHAR(20)
)
BEGIN
	select * from data where p_game_name = game_name and p_game_id = game_id order by ts desc;
END$$
DELIMITER;
