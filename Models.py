from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Text


Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(500))  # 
    author = Column(String(200))
    price = Column(String(50))
    availability = Column(String(100))
    isbn = Column(String(50))
    publish_date = Column(DateTime)
    image_url = Column(String(300))         # new
    rating = Column(Float)                  # new
    stock = Column(Integer)                 # new
    description = Column(Text)              # new

