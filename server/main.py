import uvicorn as uvicorn
from db.crud import getting_question
from db.database import SessionLocal, engine
from db.models import Question
from db.schemas import Base, Questions
from fastapi import Depends, FastAPI, Response
from sqlalchemy.orm import Session
from starlette import status

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def main()-> dict:
    return {'message': "Welcome  to servis vikorina"}


@app.post("/questions", status_code = 200)
async def is_creating_victorina(question: Question, response: Response, db: Session = Depends(get_db)) -> dict | None:
    num: int = question.questions_num
    question_text: Questions | str = await getting_question(num, db)
    if type(question_text) is str:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message error": question_text}
    elif question_text:
        return {"question": question_text.question}
@app.delete("/delete_db")
def delete_db():
    Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
