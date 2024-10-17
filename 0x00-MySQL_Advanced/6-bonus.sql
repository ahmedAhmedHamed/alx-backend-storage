-- creates a stored procedure AddBonus that adds a new correction for a student.
-- creates a stored procedure AddBonus that adds a new correction for a student.
delimiter $$
CREATE PROCEDURE AddBonus(puser_id int,
  pproject_name varchar(255),
  pscore int)
BEGIN
  if (select not exists(select id from projects where name=pproject_name)) THEN
    INSERT INTO projects (name) VALUES (pproject_name);
  END IF;

  INSERT INTO corrections (user_id, project_id, score) VALUES (puser_id, (select id from projects where name=pproject_name), pscore);
END $$
delimiter ;

