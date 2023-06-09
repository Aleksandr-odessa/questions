from pydantic import BaseModel


class Question(BaseModel):
    questions_num: int
