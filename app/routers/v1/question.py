from fastapi.routing import APIRouter

question = APIRouter()


@question.post("")
async def question_post(
        questions_num: int
):
    ...
