-- Вывести всех customers у которых FistName = 'Mark' и LastName = 'Taylor' или
-- FirstName = 'Frank' и LastName = 'Harris'
-- В предложении WHERE для объединения нескольких условий можно использовать
-- операторы: AND и OR.

SELECT *
FROM customers
WHERE FirstName = 'Mark' and LastName = 'Taylor' OR FirstName = 'Frank' and LastName = 'Harris';