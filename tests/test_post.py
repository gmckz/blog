from lib.post import Post

"""
Post constructs with an id, name and genre
"""
def test_post_constructs():
    post = Post(1, "Test Post", "Test Genre")
    assert post.id == 1
    assert post.title == "Test Post"
    assert post.post_content == "Test Genre"
    assert post.comments == None

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Test Post", "Test Genre")
    assert str(post) == "Post(Test Post, Test Genre, None)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test Post", "Test Genre")
    post2 = Post(1, "Test Post", "Test Genre")
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/post.py
    # And see what happens when you run this test again.
