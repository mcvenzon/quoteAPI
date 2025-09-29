# main.py
from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    "Do one thing every day that scares you.",
    "Stay hungry, stay foolish.",
    "Success is not final, failure is not fatal.",
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do."
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quotes API"}

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}
