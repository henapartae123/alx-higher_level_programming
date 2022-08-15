-- lists all cities in the databse hbtn_0d_usa in ascending order
SELECT c.`id`, c.`name`, s.`name`
 FROM `cities` AS cities
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
