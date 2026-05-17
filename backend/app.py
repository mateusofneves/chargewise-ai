from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import perguntar_chatbot

app = FastAPI()


class Pergunta(BaseModel):
    mensagem: str


@app.get("/")
def home():
    return {"status": "ChargeWise AI online"}


@app.post("/chat")
def chat(pergunta: Pergunta):
    resposta = perguntar_chatbot(pergunta.mensagem)

    return {
        "resposta": resposta
    }
