-- 조회
SELECT * FROM songs;

-- 정렬
SELECT * FROM songs ORDER BY title DESC;

-- 필터링
SELECT * FROM songs WHERE genre = 'Pop';

-- 조건부 조회
SELECT * FROM songs WHERE duration >= 300;