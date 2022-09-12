-- lists all genres from hbtn_0d_shows
-- displays the number of shows linked to each

SELECT genres.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS genres
       INNER JOIN `tv_show_genres` AS tv_shows
       ON genres.`id` = tv_shows.`genre_id`
 GROUP BY genres.`name`
 ORDER BY `number_of_shows` DESC;
