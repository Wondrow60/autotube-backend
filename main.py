from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Veri modeli (Email almak için)
class Email(BaseModel):
    email: str

# POST endpoint'i
@app.post("/early-access")
def collect_email(email: Email):
    print(f"Gelen e-posta: {email.email}")
    return {"message": "Kaydınız alındı!"}
