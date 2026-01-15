from flaskr import db
from sqlalchemy import Column, Integer, String

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(String(200))
    user_name = Column(String(20))