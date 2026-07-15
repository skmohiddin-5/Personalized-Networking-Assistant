from fastapi import FastAPI
from pydantic import BaseModel

from backend.model import generate_starters
from backend.wiki import get_fact
from backend.history import save_history, load_history

app = FastAPI()


class UserInput(BaseModel):
    event: str
    interests: str


@app.get("/")
def home():
    return {"message": "Personalized Networking Assistant API is running!"}


@app.post("/generate")
def generate(data: UserInput):
    starters = generate_starters(data.event, data.interests)

    save_history(
        data.event,
        data.interests,
        starters
    )

    return {
        "conversation_starters": starters
    }


@app.get("/fact/{topic}")
def fact(topic: str):
    return {
        "fact": get_fact(topic)
    }


@app.get("/history")
def history():
    return load_history()