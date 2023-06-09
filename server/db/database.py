from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user_quest:password_quest1206@db:5432/database_quest"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
SQLITE_DATABASE_URL = 'sqlite:///db/sqlite_questions.db'
engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
