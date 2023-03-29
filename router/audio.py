import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status
import PyPDF2
import pyttsx3
import os
import secrets
router = APIRouter()


@router.get("/pdf-to-audio")
async def audio():
    return {"sdf": "dfb"}


def speak_pdf(mod_text):
    FILEPATH = "audiofiles/"
    shutil.rmtree(FILEPATH)
    audio_engine = pyttsx3.init()
    audio_engine.getProperty("rate")
    audio_engine.setProperty("rate", 175)
    v = audio_engine.getProperty("voices")
    audio_engine.setProperty("voice", v[0].id)
    EXTENSION = ".mp3"
    # file save at audio files location
    if not os.path.exists(FILEPATH):
        os.makedirs(FILEPATH)
    audio_engine.save_to_file(mod_text, FILEPATH+secrets.token_hex(4)+EXTENSION)
    audio_engine.runAndWait()
    audio_engine.say(mod_text)
    audio_engine.runAndWait()
    audio_engine.stop()

@router.post("/pdf-to-audio")
async def audio(file: UploadFile = File(...)):
    name = file.filename
    if name.split(".")[1] != "pdf":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="file is not PDF")

    # reading the PDF file
    reader = PyPDF2.PdfReader(file.file)
    for i in range(0, len(reader.pages)):
        text = reader.pages[i].extract_text()
        mod_text = text.replace("\n", "")
        speak_pdf(mod_text)
        return mod_text
