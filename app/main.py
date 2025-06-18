# transcription-api/app/main.py

from fastapi import FastAPI, UploadFile, File
from app.services.whisper_service import transcribe_audio

app = FastAPI(title="Whisper Voice Translation API")

@app.post("/voice-to-text/")
async def voice_to_text(file: UploadFile = File(...)):
    result = await transcribe_audio(file)
    return {
        "translated_text": result["text"],
        "original_language": result["language"],
        "segments": result["segments"]
    }
