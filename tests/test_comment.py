from lib.comment import Comment

"""
Comment constructs with an id, name and genre
"""
def test_comment_constructs():
    comment = Comment(1, "test contents", "test author", 1)
    assert comment.id == 1
    assert comment.comment_content == "test contents"
    assert comment.author_name == "test author"
    assert comment.post_id == 1

"""
We can format comments to strings nicely
"""
def test_comments_format_nicely():
    comment = Comment(1, "test contents", "test author", 1)
    assert str(comment) == "Comment(test contents, test author, 1)"


"""
We can compare two identical comments
And have them be equal
"""
def test_comments_are_equal():
    comment1 = Comment(1, "test contents", "test author", 1)
    comment2 = Comment(1, "test contents", "test author", 1)
    assert comment1 == comment2

