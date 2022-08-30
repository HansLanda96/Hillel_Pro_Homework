SELECT albums.Title as Album,
       genres.Name as Genre,
       tracks.Composer as Artist,
       SUM(tracks.Milliseconds)/60000 as "Duration(Minues)",
       SUM(tracks.Bytes)/1048576 as "Size(MB)",
       ROUND(SUM(tracks.UnitPrice), 2) as "AlbumPrice",
       COUNT(tracks.Name) as "Amount of tracks"

FROM tracks
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
INNER JOIN genres ON tracks.GenreId = genres.GenreId
INNER JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
WHERE media_types.Name = 'MPEG audio file'
GROUP BY tracks.AlbumId
ORDER BY genres.Name, tracks.Composer;





