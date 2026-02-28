import os
import sqlalchemy
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DATABASE_URL', 'sqlite:///StudyVerse.db')
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

print(f"Connecting to: {db_url.split('@')[-1]}") # Log host only for safety

try:
    engine = sqlalchemy.create_all_engine if hasattr(sqlalchemy, 'create_all_engine') else sqlalchemy.create_engine
    engine = sqlalchemy.create_engine(db_url)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(f"Connection successful: {result.scalar()}")
except Exception as e:
    print(f"Connection failed: {e}")
