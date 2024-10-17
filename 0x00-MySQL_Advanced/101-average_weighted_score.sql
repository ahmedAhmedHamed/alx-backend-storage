-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- need to:
-- get the ids of all students
-- call the solution of 100 with the id of each student.
delimiter $$
drop procedure if exists ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE studentId int;
  DECLARE done INT DEFAULT FALSE;
  DECLARE cursorStudentIds CURSOR FOR SELECT id FROM users;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  
  
  OPEN cursorStudentIds;
  read_loop: LOOP
    FETCH cursorStudentIds INTO studentId;
    IF done THEN
      LEAVE read_loop;
    END IF;
    CALL ComputeAverageWeightedScoreForUser(studentId);
  END LOOP;
    
  CLOSE cursorStudentIds;
END $$
delimiter ;

