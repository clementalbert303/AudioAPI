# 🎙️ Speech-to-Text Studio

> Application web de transcription audio automatique basée sur le modèle **OpenAI Whisper**.

Speech-to-Text Studio permet de transformer un enregistrement audio ou une entrée microphone en **texte transcrit automatiquement** grâce à l'intelligence artificielle.

Ce projet illustre l'intégration d'un modèle de reconnaissance vocale dans une application web légère basée sur **FastAPI** et **Gradio**.

---

## 🌐 Démo & Documentation

- 🎙️ **Application Gradio :** https://audioapi-erh5.onrender.com/app
- 📚 **Documentation interactive :** https://audioapi-erh5.onrender.com/docs

---

## ⚙️ Fonctionnement

L'application suit un pipeline simple pour transformer la voix en texte :

```text
🎙️ Micro / Fichier audio
          │
          ▼
   🖥️ Interface Gradio
          │
          ▼
    ⚡ Serveur FastAPI
          │
          ▼
     🤖 Whisper Tiny
          │
          ▼
    📝 Texte transcrit



## 🛠️ Stack Technique

- **Langage :** Python 3.10
- **IA & Audio :** OpenAI Whisper, PyTorch, FFmpeg
- **Web & UI :** FastAPI, Gradio, Uvicorn
- **DevOps :** Docker, Render, Git

---