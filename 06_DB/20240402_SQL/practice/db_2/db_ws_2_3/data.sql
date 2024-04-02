SELECT * FROM hotels;

UPDATE hotels
SET grade = UPPER(grade);
SELECT grade FROM hotels;

CREATE TABLE customers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT
);



CREATE TABLE reservations(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  room_num INTEGER,
  check_in TEXT,
  check_out TEXT,
  FOREIGN KEY (room_num)
    REFERENCES hotels (room_num),
  FOREIGN KEY (customer_id)
    REFERENCES customers (id)
);

INSERT INTO customers
VALUES
(1, '홍길동', 'abc@example.com'),
(2, '박지영', 'abcd@example.com'),
(3, '김미영', 'abce@example.com'),
(4, '이철수', 'abcf@example.com');

INSERT INTO reservations
VALUES
  (1, 1, 101, '2024-03-20', '2024-03-25'),
  (2, 2, 202, '2024-03-21', '2024-03-26'),
  (3, 3, 303, '2024-03-22', '2024-03-27'),
  (4, 4, 404, '2024-03-23', '2024-03-28');

SELECT * FROM customers;
SELECT * FROM reservations;
