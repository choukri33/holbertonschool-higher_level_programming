-- Script to list all shows and their linked genres from the hbtn_0d_tvshows database
SELECT tv_shows.title, COALESCE(tv_genres.name, NULL) AS name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;