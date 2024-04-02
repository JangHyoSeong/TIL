CREATE TABLE zoo(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  eat TEXT,
  weight INTEGER,
  height INTEGER,
  age INTEGER
);

INSERT INTO zoo
VALUES
  (1, 'Lion', 'Meat', 200, 120, 5),
  (2, 'Elephant', 'Plants', 5000, 300, 15),
  (3, 'Giraffe', 'Leaves', 1500, 550, 10),
  (4, 'Monkey', 'Fruits', 50, 60, 8);

SELECT * FROM zoo;