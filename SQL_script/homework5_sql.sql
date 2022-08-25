--Написать SELECT запрос для подсчёта общей суммы треков и их количества
--сгруппировав данные по TrackId.

SELECT TrackId, SUM(UnitPrice) as TotalPrice, SUM(Quantity) as TotalQuant
FROM invoice_items
GROUP BY TrackId;