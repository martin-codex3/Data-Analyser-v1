from fastapi import FastAPI

app = FastAPI()

app.get("/")


async def greeting() -> str:
    return "hello there ladies"
