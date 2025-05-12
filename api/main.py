from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Email(BaseModel):
    email: str

@app.post("/early-access")
async def early_access(email: Email):
    print(f"Gelen e-posta: {email.email}")
    return {"message": "Kaydınız alındı!"}
