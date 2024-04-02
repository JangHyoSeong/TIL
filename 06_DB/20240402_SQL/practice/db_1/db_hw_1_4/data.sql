-- 1.
SELECT Name FROM tracks WHERE Name LIKE '%love%';

-- 2.
SELECT * FROM tracks WHERE GenreId = 1 and Milliseconds >= 300000 ORDER BY UnitPrice DESC;

-- 3.
SELECT
  GenreId, COUNT(*) AS 'TotalTracks'
FROM
  tracks
GROUP BY
  GenreId;

-- 4.
SELECT
  GenreID, SUM(UnitPrice) AS TotalPrice
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;