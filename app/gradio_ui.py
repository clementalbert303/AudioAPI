import gradio as gr
from app.services import transcribe_audio_file


def build_gradio_app() -> gr.Blocks:
    """Construit et retourne l'interface Gradio."""
    demo = gr.Interface(
        fn=transcribe_audio_file,
        inputs=gr.Audio(
            sources=["microphone", "upload"],
            type="filepath",
            label="Microphone ou fichier audio (.wav, .mp3)",
        ),
        outputs=gr.Textbox(label="Transcription", lines=4),
        title="🎙️ Speech-to-Text Studio",
        description="Interface Gradio intégrée au service FastAPI.",
        theme="soft",
    )
    return demo