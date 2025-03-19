import gradio as gr
import torch
import time
from fpdf import FPDF
from model import load_whisper_model  # Import model loader
import os

# ✅ Allowed Whisper models
ALLOWED_MODELS = ["tiny", "base", "medium"]  

# Check for device availability
device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model(model_name_or_path):
    """Load Whisper model either from predefined options or user-uploaded model file."""
    try:
        if model_name_or_path in ALLOWED_MODELS:
            model = load_whisper_model(model_name_or_path) 
        else:
            model = load_whisper_model(model_name_or_path)  # For custom models

        # Move model to GPU if available, otherwise CPU
        if torch.cuda.is_available():
            model = model.to("cuda")
        else:
            model = model.to("cpu")

        return model
    except Exception as e:
        return f"❌ Error loading model: {str(e)}"

def transcribe_audio_file(audio_file_path, model):
    try:
        whisper_model = load_model(model)
        if isinstance(whisper_model, str):
            return whisper_model  # Error message
        
        result = whisper_model.transcribe(str(audio_file_path))
        return result.get("text", "⚠️ No transcription available.")
    except Exception as e:
        return f"❌ Error: {str(e)}"

def transcribe_audio_with_time(audio_file_path, model):
    if not audio_file_path:
        return "⚠️ No audio file provided.", 0, ""

    start_time = time.time()
    transcription = transcribe_audio_file(audio_file_path, model)
    end_time = time.time()
    transcription_time = end_time - start_time

    formatted_output = f"📝 Transcription:\n\n{transcription}"
    return formatted_output, round(transcription_time, 3), transcription

# 📥 Generate TXT or PDF Report
def clean_text(text):
    return text.encode("ascii", "ignore").decode()

def generate_report_file(text, file_format="txt"):
    filename = f"structured_report.{file_format}"
    text = clean_text(text)

    if file_format == "txt":
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
    elif file_format == "pdf":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(200, 10, text)
        pdf.output(filename, "F")

    return filename

def process_audio(audio_file, model, file_format):
    transcription_output, transcription_time, transcription_text = transcribe_audio_with_time(audio_file, model)

    if not transcription_text.strip():
        return "⚠️ No valid transcription available.", 0, "", None

    report_content = f"Structured Report\n\n{transcription_text}\n\nProcessing Time: {transcription_time:.3f} seconds"
    report_file = generate_report_file(report_content, file_format)

    return transcription_output, transcription_time, report_content, report_file

# 🚀 Gradio Interface
demo = gr.Interface(
    fn=process_audio,
    inputs=[
        gr.Audio(type="filepath", label="🎵 Upload Audio File"),
        gr.Dropdown(
            choices=ALLOWED_MODELS,
            value="medium",
            label="🤖 Select a Whisper Model",
            info="Select a model for transcription. The 'tiny' model offers faster inference at the cost of lower accuracy. The 'base' model strikes a balance between speed and accuracy, while 'medium' provides the best accuracy but may take longer to process."
        ),
        gr.Radio(
            choices=["txt", "pdf"],
            value="txt",
            label="📄 Report Format",
            info="Choose the format for your transcription report. TXT is a basic text file, and PDF provides a more structured, printable report."
        ),
    ],
    outputs=[
        gr.Textbox(label="📝 Transcribed Report"),
        gr.Number(label="⏳ Processing Time (seconds)", precision=3),
        gr.Textbox(label="📑 Structured Report"),
        gr.File(label="📥 Download Report"),
    ],
    title="🎙️ AI-Powered Audio Report Generator",
    description=(
        "Upload an **audio file** 🎵 and select a **Whisper model** for transcription. "
        "You can choose from pre-trained models (Tiny, Base, Medium) depending on your need for speed and accuracy. "
        "For faster transcription, select 'tiny'. If you need better accuracy, choose 'medium'. The 'base' model offers a balance between the two. "
        "The transcription will be converted into a **structured report** 📑 available for download in **TXT** or **PDF** format."
    ),
    theme="default",
)

# 🚀 Launch App
demo.launch(debug=True, share=True)
