-- a script that creates a table called first_table in the current database
-- if doesn't exist
-- table has one row and 2 columns; id and name
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
