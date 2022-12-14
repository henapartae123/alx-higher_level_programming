-- lists all shows and all genres linked to that show
SELECT tv_shows.`title`, genres.`name`
  FROM `tv_shows` AS tv_shows
       LEFT JOIN `tv_show_genres` AS shows
       ON tv_shows.`id` = shows.`show_id`

       LEFT JOIN `tv_genres` AS genres
       ON shows.`genre_id` = genres.`id`
 ORDER BY tv_shows.`title`, genres.`name`;
 