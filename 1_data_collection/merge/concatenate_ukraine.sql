ATTACH 'ukraine_defiance_2022_export.db' AS defiance_db;
ATTACH 'ukraine_hope_2022_2023_export.db' AS hope_db;
ATTACH 'ukraine_fatigue_2023_export.db' AS fatigue_db;
ATTACH 'ukraine_anxiety_2024_export.db' AS anxiety_db;
ATTACH 'ukraine_acceptance_2024_2025_export.db' AS acceptance_db;
ATTACH 'ukraine_betrayal_despair_2025_export.db' AS betrayal_db;
ATTACH 'ukraine_selfreliance_2025_2026_export.db' AS selfreliance_db;

DROP TABLE IF EXISTS main.yt_comment_data;

CREATE TABLE main.yt_comment_data AS
SELECT * FROM defiance_db.yt_comment_data
UNION ALL
SELECT * FROM hope_db.yt_comment_data
UNION ALL
SELECT * FROM fatigue_db.yt_comment_data
UNION ALL
SELECT * FROM anxiety_db.yt_comment_data
UNION ALL
SELECT * FROM acceptance_db.yt_comment_data
UNION ALL
SELECT * FROM betrayal_db.yt_comment_data
UNION ALL
SELECT * FROM selfreliance_db.yt_comment_data;

DETACH defiance_db;
DETACH hope_db;
DETACH fatigue_db;
DETACH anxiety_db;
DETACH acceptance_db;
DETACH betrayal_db;
DETACH selfreliance_db;
