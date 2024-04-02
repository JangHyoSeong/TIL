-- 1
SELECT AVG(age) AS 'average_age' FROM users;

-- 2
SELECT country, COUNT(*) AS user_count
FROM users
GROUP BY country;

-- 3
SELECT * FROM users WHERE balance = (SELECT MAX(balance) FROM users);

-- 4
SELECT country, AVG(balance) AS avg_balance
FROM users
GROUP BY country;

-- 5
SELECT (MAX(balance) - MIN(balance)) AS balance_difference FROM users;