-- creates table first_table if does not exist and adds one row
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
INSERT INTO first_table (id, name) VALUES (89, "Best School");