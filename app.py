from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog.sql")

    def run(self, post_id):
        post_repository = PostRepository(self._connection)
        post_and_comments = post_repository.find_post_with_comments(post_id)
        print(post_and_comments.title)
        print(post_and_comments.post_content)
        for comment in post_and_comments.comments:
            print(comment.comment_content)
            print(comment.author_name)


if __name__ == '__main__':
    app = Application()
    post_id = input("To see a post and its comments, enter the post id   ")
    app.run(post_id)


#Write a small program in app.py using the class PostRepository 
# to print out the data of one post with its comments to the terminal 