

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)
class Post:
    def __init__(self, id, title, post_content, comments = None):
        self.id = id
        self.title = title
        self.post_content
        self.comments = [] or comments

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"..."

class Comment:
    def __init__(self, id, comment_content, author_name, post_id):
        self.id = id
        self.comment_content = comment_content
        self.author_name = author_name
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"..."

# Repository class
# (in lib/student_repository.py)
class PostRepository:

    def __init__(self,connection):
        self._connection = connection

    def find_post_with_comments(self, post_id):
        pass

```


## 6. Write Test Examples

```
"""
When we call #find_post_with_comments 
we get the post object containing list of comments
"""
def test_find_post_with_comments():
    post_repository = PostRepository()
    result = post_repository.find_post_with_comments()
    assert result == Post("title1", "contents1, [Comment(1, 'comment1', 'author1', 1), Comment(2, 'comment2', 'author1', 1)] )
```