from json import JSONDecodeError

import httpx
from config import ADRES, FIELDS
from config_log import logger


async def request_questions(number: int) -> httpx.Response | str:
    async with httpx.AsyncClient() as client:
        try:
            question: httpx.Response = await client.get(f'{ADRES}{number}')
            question.raise_for_status()
        except httpx.HTTPError as exc:
            logger.error(f"HTTP Exception for {exc.request.url} - {exc}")
            return f"HTTP Exception for {exc.request.url} - {exc}"
    return question



def parsing_json(question: httpx.Response) -> list | str:
    try:
        responce_json = question.json()
    except JSONDecodeError:
        logger.error('Decoding JSON has failed')
        return "Decoding JSON has failed"
    questions: list = [{q: quest[q]for q in FIELDS} for quest in responce_json]
    return questions
