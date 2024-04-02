CREATE TABLE songs(
  id INTEGER PRIMARY KEY,
  title TEXT,
  artist TEXT,
  album TEXT,
  genre TEXT,
  duration INTERGER
);


INSERT INTO
  songs(title, artist, album, genre, duration)
VALUES
  ('Song 1', 'Artist 1', 'Album 1', 'genre 1', 100),
  ('Song 2', 'Artist 2', 'Album 2', 'genre 2', 100),
  ('Song 3', 'Artist 3', 'Album 3', 'genre 3', 100),
  ('Song 4', 'Artist 4', 'Album 4', 'genre 4', 100),
  ('Song 5', 'Artist 5', 'Album 5', 'genre 5', 100);


UPDATE songs
SET title = 'New Title'
WHERE title = 'Song 1';