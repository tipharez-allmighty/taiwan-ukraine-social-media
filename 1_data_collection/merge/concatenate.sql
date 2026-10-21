ATTACH 'ukraine_full.db' AS ukraine_db;
ATTACH 'taiwan_full.db' AS taiwan_db;
ATTACH 'full_data.db' AS full_db;

DROP TABLE IF EXISTS full_db.yt_comment_data;
CREATE TABLE full_db.yt_comment_data AS
SELECT * FROM ukraine_db.yt_comment_data
UNION ALL
SELECT * FROM taiwan_db.yt_comment_data;

DETACH ukraine_db;
DETACH taiwan_db;
DETACH full_db; 
