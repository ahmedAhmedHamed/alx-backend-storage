-- decreases the quantity of an item after adding a new order.
-- decreases the quantity of an item after adding a new order.
CREATE TRIGGER ins_order AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET
quantity = quantity - new.number
WHERE name=new.item_name;

