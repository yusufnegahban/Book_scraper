from sqlalchemy import create_engine
from models import Base

# Replace with your actual PostgreSQL config
engine = create_engine('postgresql://postgres:10011001@localhost:5432/books_db')

# Create all tables
Base.metadata.create_all(engine)

print("✅ Table(s) created successfully.")
