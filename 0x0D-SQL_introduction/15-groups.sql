-- a script that lists the number of records with the same score in the table
-- second_table of the database hbtn_0c_0
-- the result displays the score and the number of records for the score
-- with the label number
-- the list is sorted by the number of records in descending order

SELECT score,
COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
