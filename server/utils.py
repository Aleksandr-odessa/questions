import httpx
from config import ADRES, FIELDS


async def request_questions(number: int) -> list:
    async with httpx.AsyncClient() as client:
        ques = await client.get(f'{ADRES}{number}')
    return pars_json(ques.json())


def pars_json(question: dict) -> list:
    questions = []
    for quest in question:
        dict_temp = {q: quest[q]for q in FIELDS}
        questions.append(dict_temp)
    return questions
