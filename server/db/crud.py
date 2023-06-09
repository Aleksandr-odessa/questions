from sqlalchemy.exc import IntegrityError

from db.schemas import Questions
from utils import request_questions
from datetime import datetime


async def add_question(num: int, db) -> str | None:
    global now
    questions: list = await request_questions(num)
    for quest in questions:
        time = datetime.strptime(quest['created_at'][:19], '%Y-%m-%dT%H:%M:%S')
        try:
            question = Questions(id=quest['id'], question=quest['question'],
                                 answer=quest['answer'], data_created=time)
            db.add(question)
            db.flush()
            now = question.num
        except IntegrityError:
            question_: list = await request_questions(1)
            questions.append(question_[0])
            db.rollback()
    db.commit()
    previous = db.get(Questions, now - 1)
    if previous:
        return previous.question
