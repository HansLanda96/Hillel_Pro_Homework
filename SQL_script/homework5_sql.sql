--Написать SELECT запрос для подсчёта общей суммы треков и их количества
--сгруппировав данные по TrackId.

SELECT TrackId, SUM(UnitPrice) as TotalPrice, COUNT(TrackId) as TotalTrackId
FROM invoice_items
GROUP BY TrackId;