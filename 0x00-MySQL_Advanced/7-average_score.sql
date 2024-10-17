-- computes and store the average score for a student. Note: An average score can be a decimal
-- computes and store the average score for a student. Note: An average score can be a decimal
delimiter $$
CREATE PROCEDURE ComputeAverageScoreForUser(puser_id int)
BEGIN
  UPDATE users
  SET
  average_score = (SELECT AVG(score)
  FROM corrections
  WHERE user_id = puser_id)
  where id = puser_id;
END $$
delimiter ;

