from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# E-posta modelini oluşturuyoruz
class Email(BaseModel):
    email: str

# /early-access endpoint'ine sadece POST isteği alıyoruz
@app.post("/early-access")
def collect_email(email: Email):
    print(f"Gelen e-posta: {email.email}")
    return {"message": "Kaydınız alındı!"}
