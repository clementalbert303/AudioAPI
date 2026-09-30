import os
import whisper

# Chargement unique du modèle
model = whisper.load_model("tiny")


def transcribe_audio_file(file_path: str) -> str:
    """Prend un chemin de fichier audio et renvoie le texte transcrit."""
    if not file_path or not os.path.exists(file_path):
        return "Aucun fichier audio valide fourni."

    result = model.transcribe(file_path)
    return result["text"]