ATTACH 'taiwan_anxiety_2024_export.db' AS export_db;

CREATE TABLE export_db.yt_comment_data AS
SELECT
    'thread_only' AS row_type,
    'anxiety' AS timeline,
    'Taiwan' AS topic,
    v.id             AS video_id,
    v.title          AS video_title,
    v.description    AS video_description,
    t.id             AS thread_id,
    t.author         AS thread_author,
    t.text_original  AS thread_text_original,
    t.like_count     AS thread_like_count,
    t.total_reply_count,
    t.published_at   AS thread_published_at,
    NULL AS comment_id,
    NULL AS comment_author,
    NULL AS comment_text_original,
    NULL AS comment_like_count,
    NULL AS comment_published_at
FROM threads t
JOIN videos v ON v.id = t.video_id
UNION ALL
SELECT
    'thread_with_comment' AS row_type,
    'anxiety' AS timeline,
    'Taiwan' AS topic,
    v.id             AS video_id,
    v.title          AS video_title,
    v.description    AS video_description,
    t.id             AS thread_id,
    t.author         AS thread_author,
    t.text_original  AS thread_text_original,
    t.like_count     AS thread_like_count,
    t.total_reply_count,
    t.published_at   AS thread_published_at,
    c.id             AS comment_id,
    c.author         AS comment_author,
    c.text_original  AS comment_text_original,
    c.like_count     AS comment_like_count,
    c.published_at   AS comment_published_at
FROM comments c
JOIN threads t ON t.id = c.thread_id
JOIN videos v  ON v.id = t.video_id
ORDER BY row_type DESC, comment_published_at;

DETACH export_db;
