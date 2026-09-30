# 🎙️ Speech-to-Text API & Studio

Une API REST performante et modulaire de transcription audio basée sur **OpenAI Whisper**, couplée à une interface utilisateur interactive **Gradio**, conteneurisée avec **Docker** et hébergée sur **Render**.

- **Gradio Studio :** https://audioapi-erh5.onrender.com/app
- **Swagger UI :** https://audioapi-erh5.onrender.com/docs

---

## 🛠️ Technologies & Bibliothèques utilisées

- **FastAPI** : Framework Python moderne et performant pour orchestrer l'API REST.
- **OpenAI Whisper (`tiny`)** : Modèle de reconnaissance vocale avancé, optimisé pour la consommation mémoire.
- **Gradio** : Interface web interactive intégrée directement dans FastAPI pour l'enregistrement micro et l'import de fichiers.
- **Uvicorn** : Serveur ASGI ultra-rapide exécutant l'application.
- **Docker** : Conteneurisation complète garantissant la portabilité entre l'environnement local et la production.

---

## 📁 Architecture du Projet

Le projet suit une structure modulaire séparant la logique métier, l'interface graphique et le routage API :

```text
.
├── app/
│   ├── __init__.py
│   ├── main.py          # Orchestration FastAPI, CORS et montage Gradio
│   ├── services.py      # Chargement de Whisper et logique de transcription
│   └── gradio_ui.py     # Définition de l'interface utilisateur Gradio
├── Dockerfile           # Configuration du conteneur
└── requirements.txt     # Dépendances Python