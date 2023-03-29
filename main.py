from fastapi import FastAPI
from starlette import status
from starlette.responses import RedirectResponse

import models
from database import engine
from router import audio
import pyttsx3
import PyPDF2

app = FastAPI()

app.include_router(audio.router)

@app.get("/")
def pdf_audio():
    return RedirectResponse(url="/pdf-to-audio", status_code=status.HTTP_302_FOUND)

models.Base.metadata.create_all(bind=engine)
