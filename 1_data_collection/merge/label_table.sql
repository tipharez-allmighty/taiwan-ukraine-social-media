ATTACH 'full_data.db' as full_data;

ALTER TABLE full_data.yt_comment_data
ADD COLUMN id INTEGER;
UPDATE full_data.yt_comment_data
SET id = rowid;
CREATE UNIQUE INDEX full_data.idx_yt_comment_data_id ON yt_comment_data(id);

CREATE TABLE full_data.yt_comment_label (
  id INTEGER PRIMARY KEY,
  run_number INTEGER,
  labeler TEXT,
  yt_data_id INTEGER,
  critical_ukraine BOOLEAN,
  supportive_ukraine BOOLEAN,
  critical_taiwan BOOLEAN,
  supportive_taiwan BOOLEAN,
  disappointment_with_us BOOLEAN,
  blame_nato_expansion BOOLEAN,
  FOREIGN KEY (yt_data_id) REFERENCES yt_comment_data(id),
  UNIQUE(yt_data_id, run_number)
);
DETACH full_data;
