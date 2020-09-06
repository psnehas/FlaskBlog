import json
from flask import flash
from flaskblog import db
from flaskblog.models import Post, User


with open('./posts.json') as f:
  data = json.load(f)
  for post in data:
      title = post['title']
      content = post['content']
      author = post['user_id']
      user_post = Post(title = title, content=content, author=User.query.get_or_404(author))
      db.session.add(user_post)
      db.session.commit()
  print("All posts created!")
