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
# with open("I20_Avula_Manoj.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     text = reader.pages[0].extract_text()
# engine1 = pyttsx3.init()
# v = engine1.getProperty("voices")
# engine1.setProperty("voice", v[0].id)
# rate = engine1.getProperty("rate")
# engine1.setProperty("rate", 175)
# engine1.say(text)
# engine1.say('My current speaking rate is ' + str(rate))
# engine1.runAndWait()
# engine1.stop()
