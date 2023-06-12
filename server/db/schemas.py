from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ ='questions'
    num = Column(Integer, autoincrement=True, primary_key=True)
    id = Column(Integer, unique=True)
    question = Column(String)
    answer = Column(String)
    data_created = Column(Date)
