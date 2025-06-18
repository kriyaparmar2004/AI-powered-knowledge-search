# transcription-api/app/services/whisper_service.py

import whisper
import io
import tempfile
import shutil
import ffmpeg

# ffmpeg.input('input.mp4').output('output.avi').run()

# Load the model once at module level
model = whisper.load_model("large")

async def transcribe_audio(file):
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        await file.seek(0)
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    # Transcribe using the file path
    result = model.transcribe(tmp_path, task="translate")

    # Optionally, delete the temp file
    # os.remove(tmp_path)

    return {
        "text": result["text"],
        "language": result["language"],
        "segments": result.get("segments", [])
    }
