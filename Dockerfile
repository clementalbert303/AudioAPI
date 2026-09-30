# 1. Utilisation d'une image Python ultra-Légère
FROM python:3.10-slim

# Évite la création de fichiers .pyc et force l'affichage direct des logs
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 2. Installation de ffmpeg (indispensable pour Whisper/Gradio)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Optimisation Render : Pré-téléchargement du modèle Whisper lors du build Docker
# Cela évite que le conteneur ne télécharge le modèle à chaque redémarrage et dépasse la limite de RAM
RUN python -c "import whisper; whisper.load_model('tiny')"

# 5. Copie du code source
COPY . .

# 6. Exposition du port et commande de lancement
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]