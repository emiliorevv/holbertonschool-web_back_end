-- Script that creates a stored procedure ComputeAverageScoreForUser

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);


    SELECT IFNULL(AVG(score), 0) INTO avg_score 
    FROM corrections 
    WHERE corrections.user_id = user_id;
    UPDATE users 
    SET average_score = avg_score 
    WHERE id = user_id;
END $$

DELIMITER ;