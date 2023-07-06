# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: students

Columns:
id | name | cohort_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

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