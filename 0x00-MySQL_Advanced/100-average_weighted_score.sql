-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
-- need to:
-- get all the corrections of the student
-- and for each correction:
-- increment a counter
-- get its associated project and multiply the score by the weight and add to the total sum
-- after getting the sum of the weights
-- return the division 
delimiter $$
drop procedure if exists ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(puser_id int)
BEGIN
  DECLARE projectWeight int;
  DECLARE counter int;
  DECLARE res float;
  DECLARE projectId int;
  DECLARE studentScore float;
  DECLARE done INT DEFAULT FALSE;
  DECLARE cursorCorrections CURSOR FOR SELECT project_id, score FROM corrections
                                       where user_id = puser_id;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  set res = 0;
  set counter = 0;
  
  
  OPEN cursorCorrections;
  read_loop: LOOP
    FETCH cursorCorrections INTO projectId, studentScore;
    IF done THEN
      LEAVE read_loop;
    END IF;
    set projectWeight = (select weight from projects
                           where id = projectId);
    set counter = counter + (projectWeight);
    set res = (res + (projectWeight * studentScore));
    select projectWeight;
    select studentScore;
    select counter;
    END LOOP;
    
  CLOSE cursorCorrections;
  select res;
  select counter;
  IF (counter = 0) THEN
    UPDATE users
    SET
    average_score = 0
    WHERE
    id = puser_id;
  ELSE
    UPDATE users
    SET
    average_score = res / counter
    WHERE
    id = puser_id;
  END IF;
END $$
delimiter ;

