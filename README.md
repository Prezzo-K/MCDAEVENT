# Whisper ASR - Clinical Report Generation from Audio

## Overview

**Whisper ASR** is a proof-of-concept system that transcribes audio recordings from sonography sessions and generates structured clinical reports. This project leverages **Whisper** for audio transcription. The system is designed for the **MCDA GenAI event** at Saint Mary's University (SMU).

🔗 **Live Demo**: [Hugging Face Spaces - WhisperASR](https://huggingface.co/spaces/AbdiazizAden/WhisperASR)

## Problem Statement

Given an anonymized clinical audio recording (in `.wav` format), the goal is to generate a structured clinical report. The report will include information like sonography findings, patient details, and other medical data.

## Features

- **Audio Transcription**: The system uses Whisper to transcribe `.wav` audio files into text.
- **Structured Report Generation**: A report is generated based on the extracted transcription, formatted in a clinical report style.
- **Web Interface**: A simple, user-friendly interface for uploading `.wav` files and generating reports.

## Installation

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7+
- pip
- Virtual environment (optional but recommended)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/WhisperASR.git
   cd WhisperASR
   ```

2. Create a virtual environment and activate it (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download and set up the models:

   - **Whisper model** for transcription. (Please see [Whisper Documentation](https://github.com/openai/whisper) for more details)
   - Ensure the `.wav` audio files are accessible.

## Usage

### Running the Application Locally

1. Start the application:

   ```bash
   python app.py
   ```

2. A gradio interface will load in a few seconds.

3. Upload your `.wav` audio file.

4. After processing, the system will generate and display a structured clinical report.

### Files & Input

- **Input Audio**: `.wav` files for transcription.

### Example

#### Example Audio:

- `example_audio.wav` - An anonymized sonography recording.

### Output

The system will output a report similar to the structure of the provided clinical notes.

### Notes on Performance

- The **medium** Whisper model requires substantial resources and may not be available in certain environments due to limitations in the system's storage. Please use the **tiny** or **base** models for lower resource consumption.
- If you're testing on a server with storage limitations, consider using the `base` or `tiny` Whisper models.

#### ASR Metrics by Model

Below is a comparison of the ASR (Automatic Speech Recognition) metrics for the **tiny**, **base**, and **medium** Whisper models:

![ASR Metrics by Model](assets/stats_whisper.png)

-- **Metrics**:
- WER (Word Error Rate): Percentage of incorrectly recognized words. Lower WER means better accuracy.
- MER (Match Error Rate): Proportion of mismatched words. Lower MER indicates better accuracy.
- WIL (Word Information Lost): Measures lost word information. Lower WIL is preferred.
- WIP (Word Information Preserved): Proportion of preserved word information. Higher WIP is better.
- CER (Character Error Rate): Percentage of incorrect characters. Lower CER indicates better character-level accuracy.

-- **Models**: tiny, base, medium

The figure highlights the performance trade-offs between the models on the small set of the given audio files and their ground truth texts. The **medium** model offers the highest accuracy and better results but requires more computational resources, while the **tiny** model is faster but less accurate. The **base** model gives a balance between the two.

## Authors

- **Abdiaziz Muse** - [@AbdiazizAden](https://github.com/Prezzo-K)
