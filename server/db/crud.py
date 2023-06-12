from datetime import datetime

import httpx
from db.schemas import Questions
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from utils import parsing_json, request_questions


async def add_question_to_db(questions: list, db: Session) -> int:
    record_number: int = 0
    for quest in questions:
        time = datetime.strptime(quest['created_at'][:19], '%Y-%m-%dT%H:%M:%S')
        try:
            question = Questions(id=quest['id'], question=quest['question'],
                                 answer=quest['answer'], data_created=time)
            db.add(question)
            db.flush()
            record_number = question.num
        except IntegrityError:
            question_replay: list = await request_questions(1)
            questions.append(question_replay[0])
            db.rollback()
    db.commit()
    return record_number


async def getting_question(num: int, db: Session) -> Questions | str:
    questions: httpx.Response | str = await request_questions(num)
    if type(questions) is str:
        return questions
    else:
        pars_json: list | str = parsing_json(questions)
        if pars_json is str:
            return pars_json
        else:
            entry_number: int = await add_question_to_db(pars_json, db)
            previous: Questions | None = db.get(Questions, entry_number - 1)
            return previous
