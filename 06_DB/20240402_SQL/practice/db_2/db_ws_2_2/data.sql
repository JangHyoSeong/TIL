ALTER TABLE zoo
ADD COLUMN species TEXT;

PRAGMA table_info('zoo');

UPDATE zoo
SET species = 'Panthera leo', height = height * 2.54
WHERE rowid = 1;

UPDATE zoo
SET species = 'Loxodonta africana', height = height * 2.54
WHERE rowid = 2;

UPDATE zoo
SET species = 'Giraffa camelopardalis', height = height * 2.54
WHERE rowid = 3;

UPDATE zoo
SET species = 'Cebus capucinus', height = height * 2.54
WHERE rowid = 4;


SELECT * FROM zoo;