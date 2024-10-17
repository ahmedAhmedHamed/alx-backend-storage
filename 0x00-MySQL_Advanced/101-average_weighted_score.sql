-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- need to:
-- get the ids of all students
-- call the solution of 100 with the id of each student.
-- if the current id is not the same as the previous id: calculate and store the average
-- and reset the variables
-- store current id as previous id
delimiter $$
drop procedure if exists ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE projectWeight int;
  DECLARE counter int;
  DECLARE res float;
  DECLARE projectId int;
  DECLARE studentScore float;
  DECLARE puser_id int;
  DECLARE prevStudentId int;
  DECLARE done INT DEFAULT FALSE;
  DECLARE cursorStudentIds CURSOR FOR SELECT
  users.id, corrections.project_id, corrections.score FROM users 
                                  CROSS JOIN corrections
                                  ON users.id = corrections.user_id;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  set counter = 0;
  set res = 0;

  OPEN cursorStudentIds;
  read_loop: LOOP
    FETCH cursorStudentIds INTO puser_id, projectId, studentScore;
    IF done or (counter != 0 and puser_id != prevStudentId) THEN
      IF (counter = 0) THEN
    UPDATE users
    SET
    average_score = 0
    WHERE
    id = prevStudentId;
  ELSE
    UPDATE users
    SET
    average_score = res / counter
    WHERE
    id = prevStudentId;
  END IF;
      SET res = 0;
      SET counter = 0;
    END IF;
    
    IF done THEN
      LEAVE read_loop;
    END IF;
    set prevStudentId = puser_id;
    set projectWeight = (select weight from projects
                           where id = projectId);
    set counter = counter + (projectWeight);
    set res = (res + (projectWeight * studentScore));
  END LOOP;
  CLOSE cursorStudentIds;
END $$
delimiter ;

