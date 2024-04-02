DROP TABLE orders;

CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE NOT NULL,
  total_amount REAL NOT NULL
);

CREATE TABLE customer(
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);

ALTER TABLE
  orders
ADD COLUMN
  price INTEGER NOT NULL DEFAULT 0;

-- ALTER TABLE
--   orders
-- DROP COLUMN 
--   total_amount;

ALTER TABLE orders
RENAME TO new_orders;

CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE NOT NULL,
  price INTEGER NOT NULL
);

DROP TABLE new_orders;

INSERT INTO
  orders
VALUES
  (1, '2023-07-15', 500),
  (2, '2023-07-16', 600),
  (3, '2023-07-17', 700);

SELECT * FROM orders;