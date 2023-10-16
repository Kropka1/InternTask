import fastapi
from app.db import engine
app = fastapi.FastAPI()


@app.on_event("startup")
async def start_up():
    await engine.connect()

