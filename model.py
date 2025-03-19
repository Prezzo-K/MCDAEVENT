import whisper
import torch
import os

# ✅ Allowed Whisper models with custom local paths
ALLOWED_MODELS = {
    "tiny": "models/whisper_tiny.pth",
    "base": "models/whisper_base.pth",
    "medium": "models/whisper_medium.pth",
}

def load_whisper_model(model_name):
    """Load Whisper model from local weights."""
    if model_name not in ALLOWED_MODELS:
        raise ValueError(f"❌ Invalid model selected: {model_name}")

    # Path to the models folder in the Hugging Face Space repo
    model_path = ALLOWED_MODELS[model_name]

    print(f"Checking if model weights exist at: {model_path}")  # Debugging line

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"🚫 Model weights not found at {model_path}. Ensure you have saved them.")

    print(f"📥 Loading {model_name} architecture...")

    # ⚡ Load model architecture (model structure)
    model = whisper.load_model(model_name, download_root="models")  # This loads the architecture only (not weights)

    print(f"🔄 Applying saved weights from {model_path}...")

    # ⚡ Apply local weights
    state_dict = torch.load(model_path, map_location="cpu")  # Load model weights from the local file
    model.load_state_dict(state_dict, strict=False)  # Apply the weights

    return model
