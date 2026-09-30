import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import gradio as gr
from app.gradio_ui import build_gradio_app
from app.services import transcribe_audio_file

app = FastAPI(
    title="AudioAPI_app",
    description="API Speech-to-Text avec interface Gradio intégrée",
)

# 1. Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise tous les domaines externes à appeler l'API
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes HTTP
)


# 2. Route racine
@app.get("/")
def root():
    return {
        "message": "API opérationnelle",
        "swagger": "/docs",
        "gradio_app": "/app",
    }


# 3. Route API de transcription
@app.post("/transcribe")
async def api_transcribe(file: UploadFile = File(...)):
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as f:
        f.write(await file.read())

    text = transcribe_audio_file(temp_filename)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    return {"text": text}


# 4. Montage de Gradio sur /app
gradio_interface = build_gradio_app()
app = gr.mount_gradio_app(app, gradio_interface, path="/app")