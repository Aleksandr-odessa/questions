import uvicorn as uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.crud import add_question
from db.database import engine, SessionLocal
from db.models import Question
from db.schemas import Base

Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/questions")
async def process_questions(question: Question, db: Session = Depends(get_db)) -> dict:
    num: int = question.questions_num
    question_text = await add_question(num, db)
    return {"question": question_text}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
