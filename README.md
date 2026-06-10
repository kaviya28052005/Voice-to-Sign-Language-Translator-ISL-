# Voice to Indian Sign Language (ISL) Translator

## 📖 Overview

The Voice to Indian Sign Language (ISL) Translator is an assistive communication system developed to help bridge the communication gap between hearing individuals and the deaf or hard-of-hearing community. The system converts spoken words into corresponding Indian Sign Language (ISL) videos in real time.

The project uses an AI Thinker VC-02 voice recognition module for capturing speech input and a Raspberry Pi for processing, storing, and displaying sign language videos. A web-based interface was also developed to improve accessibility and user interaction.

---

## 🎯 Objectives

- Convert speech into Indian Sign Language (ISL).
- Improve communication accessibility for hearing-impaired individuals.
- Provide real-time voice-to-sign translation.
- Develop a low-cost embedded solution using Raspberry Pi.
- Create a user-friendly web interface for interaction and monitoring.

---

## 🛠️ Hardware Components

| Component | Purpose |
|------------|----------|
| Raspberry Pi | Main processing and storage unit |
| AI Thinker VC-02 | Voice recognition module |
| Microphone | Captures user speech |
| Display Monitor | Displays sign language videos |
| Speaker | Provides audio feedback |

---

## 💻 Software Requirements

- Python 3.x
- Tkinter
- SpeechRecognition
- pyttsx3
- Pillow (PIL)
- tkvideo
- PyAudio
- HTML
- CSS
- JavaScript

---

## ⚙️ System Architecture

```text
User Speech
     │
     ▼
AI Thinker VC-02
     │
     ▼
Raspberry Pi
     │
     ▼
Speech Recognition
     │
     ▼
Text Conversion
     │
     ▼
ISL Video Database
     │
     ▼
Sign Language Video Playback
     │
     ▼
Web Interface
```

---

## ✨ Features

- Real-time speech recognition
- Voice-to-Indian Sign Language conversion
- Word-level sign language translation
- Letter-by-letter fallback translation
- Digit recognition and translation
- Text-to-Speech feedback
- Interactive GUI using Tkinter
- Raspberry Pi implementation
- Web-based user interface
- Expandable sign language video database

---

## 📂 Project Structure

```text
Voice-to-ISL/
│
├── sign_videos/
│   ├── words/
│   ├── letters/
│   └── digits/
│
├── website/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── logo.jpg
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔄 Working Principle

### Step 1: Voice Input
The user speaks through a microphone connected to the system.

### Step 2: Speech Recognition
The AI Thinker VC-02 module captures the speech signal and sends it to the Raspberry Pi.

### Step 3: Speech-to-Text Conversion
Python Speech Recognition converts the captured speech into text.

### Step 4: Text Processing
The system searches for the corresponding ISL video in the database.

### Step 5: Sign Language Translation

- If a complete word video exists, it is played directly.
- If the word video is unavailable, the system displays individual letter sign videos.
- Numeric inputs are translated using digit sign videos.

### Step 6: Output Display
The translated ISL videos are displayed through the GUI and can also be accessed through the web interface.

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Voice-to-ISL.git
cd Voice-to-ISL
```

### Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 Pillow tkvideo pyaudio
```

### Run the Application

```bash
python main.py
```

---

## 📦 Required Libraries

```text
SpeechRecognition
pyttsx3
Pillow
tkvideo
pyaudio
threading
os
tkinter
```

---

## 🌐 Web Interface

A web application was developed to provide:

- Easy access to the translator
- Remote monitoring
- User-friendly interaction
- Improved accessibility

---

## 📸 Screenshots

### Main GUI
Add your GUI screenshot here.

### Web Interface
Add your webpage screenshot here.

### Hardware Setup
Add Raspberry Pi and AI Thinker VC-02 setup images here.

---

## 🔮 Future Enhancements

- Complete sentence-level translation
- AI-based sign language generation
- Offline speech recognition
- Mobile application support
- Multi-language translation
- Cloud-based sign language database
- 3D animated sign language avatar

---

## 👨‍💻 Developed By

KAVIYA M

B.E. Electronics and TeleCommunication Engineering 

### Skills

-Embedded Systems
-IoT Development
-Machine Learning
-ESP32 Programming
-Raspberry Pi
-Hardware-Software Integration

Project: Voice to Sign Language Translator Using Raspberry Pi and AI Thinker VC-02

---
⭐ If you found this project useful, please consider giving it a star on GitHub.
