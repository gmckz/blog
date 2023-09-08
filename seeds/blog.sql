-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Then, we recreate them
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  post_content text
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  author_name text,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, post_content) VALUES ('title1', 'contents1');
INSERT INTO posts (title, post_content) VALUES ('title2', 'contents2');
INSERT INTO posts (title, post_content) VALUES ('title3', 'contents3');
INSERT INTO posts (title, post_content) VALUES ('title4', 'contents4');


INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment1', 'author1', 1);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment2', 'author1', 1);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment3', 'author2', 2);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment4', 'author3', 2);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment5', 'author4', 3);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment6', 'author5', 4);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('comment7', 'author6', 4);






