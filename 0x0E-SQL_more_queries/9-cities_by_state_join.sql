-- lists all cities in the databse hbtn_0d_usa in ascending order
SELECT cities.`id`, cities.`name`, states.`name`
 FROM `cities` AS cities
       INNER JOIN `states` AS states
       ON cities.`state_id` = states.`id`
 ORDER BY cities.`id`;
