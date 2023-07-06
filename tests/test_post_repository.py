from lib.post import Post
from lib.comment import Comment
from lib.post_repository import *

"""
When we call #find_post_with_comments 
we get the post object containing list of comments
"""
def test_find_post_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    post_repository = PostRepository(db_connection)
    result = post_repository.find_post_with_comments(1)
    assert result == Post(1, "title1", "contents1", [Comment(1, 'comment1', 'author1', 1), Comment(2, 'comment2', 'author1', 1)])