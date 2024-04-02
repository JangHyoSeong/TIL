-- 1
SELECT * FROM users WHERE age >= 30 AND balance >= 1000;

-- 2
SELECT * FROM users WHERE age <= 20 AND balance <= 1000;

-- 3
SELECT * 
FROM users
WHERE
  age = (SELECT MAX(age) FROM users WHERE first_name LIKE '현%' AND country = '제주특별자치도')
  AND first_name LIKE '현%'
  AND country = '제주특별자치도';

-- 4
SELECT 
  *
FROM
  users
WHERE
  last_name = '박' AND
  age = (
    SELECT MIN(age) 
    FROM users 
    WHERE last_name = '박' AND age>=25
  )
LIMIT 1;

-- 5
SELECT *
FROM users
WHERE
  (first_name = '재은' OR 
  first_name = '영일') AND
  balance = (
    SELECT MAX(balance)
    FROM users
    where first_name = '재은' OR first_name = '영일'
  );

-- 6
SELECT u1.*
FROM users u1
JOIN (
    SELECT country, MAX(balance) AS max_balance
    FROM users
    GROUP BY country
) u2 ON u1.country = u2.country AND u1.balance = u2.max_balance
ORDER BY u1.balance DESC;

-- 7
SELECT u1.*
FROM users u1
JOIN (
    SELECT AVG(balance) AS avg_balance
    FROM users u2
    WHERE age >= 30
) u2 ON u1.balance >= u2.avg_balance
WHERE u1.age >= 30;