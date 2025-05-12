from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Email(BaseModel):
    email: str

@app.post("/early-access")
def collect_email(email: Email):
    print(f"Gelen e-posta: {email.email}")
    return {"message": "Kaydınız alındı!"}
