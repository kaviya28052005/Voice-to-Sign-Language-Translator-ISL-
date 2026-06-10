import os
import threading
import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
from tkvideo import tkvideo

# ---------------- CONFIGURATION ----------------
VIDEO_FOLDER = "sign_videos"
DIGIT_FOLDER = os.path.join(VIDEO_FOLDER, "digits")
LETTER_FOLDER = os.path.join(VIDEO_FOLDER, "letters")
WORD_FOLDER = os.path.join(VIDEO_FOLDER, "words")
SPEECH_DELAY = 1500  # milliseconds

# ---------------- INITIALIZE GUI ----------------
root = tk.Tk()
root.title("Voice to ISL")
root.geometry("900x550")
root.config(bg="white")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

# ---------------- TOP TITLE ----------------
top_frame = tk.Frame(root, bg="#1E90FF", height=60)
top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

title_label = tk.Label(
    top_frame,
    text="Voice to ISL",
    font=("Arial", 24, "bold"),
    bg="#1E90FF",
    fg="white"
)
title_label.pack(expand=True)

# ---------------- LEFT PANEL ----------------
left_frame = tk.Frame(root, bg="white", width=200)
left_frame.grid(row=1, column=0, sticky="ns", padx=20, pady=20)

left_inner_frame = tk.Frame(left_frame, bg="white")
left_inner_frame.pack(expand=True)

text_label = tk.Label(
    left_inner_frame,
    text="Click Mic to Speak",
    font=("Arial", 12),
    bg="white"
)
text_label.pack(pady=10)

# ---------------- TTS ----------------
engine = pyttsx3.init()

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS error:", e)

# ---------------- RIGHT PANEL ----------------
right_frame = tk.Frame(root, bg="white")
right_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

video_label = tk.Label(
    right_frame,
    text="Welcome to Voice to ISL Translator",
    font=("Arial", 18),
    bg="white",
    fg="black",
    wraplength=500
)
video_label.pack(expand=True)

# ---------------- LOGO ----------------
try:
    logo_img = Image.open("logo.jpg")
    logo_img = logo_img.resize((100, 100))
    logo_image = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(right_frame, image=logo_image, bg="white")
    logo_label.image = logo_image
    logo_label.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
except Exception as e:
    print("Logo not loaded:", e)

# ---------------- VIDEO PLAYBACK ----------------
def play_video_and_speak(video_path, text=""):
    if os.path.exists(video_path):
        video_label.config(image='', text='')
        player = tkvideo(video_path, video_label, loop=0, size=(400, 400))
        player.play()
        if text:
            speak(text)
    else:
        print(f"Video not found: {video_path}")

# ---------------- WORD HANDLER ----------------
def handle_word(word):
    word = word.lower()

    word_video = os.path.join(WORD_FOLDER, f"{word}.mp4")
    if os.path.exists(word_video):
        play_video_and_speak(word_video, word)
        return

    if word.isdigit():
        for digit in word:
            digit_video = os.path.join(DIGIT_FOLDER, f"{digit}.mp4")
            play_video_and_speak(digit_video, digit)
        return

    for letter in word:
        if letter.isalpha():
            letter_video = os.path.join(LETTER_FOLDER, f"{letter}.mp4")
            play_video_and_speak(letter_video, letter)

# ---------------- SPEECH PROCESSING ----------------
def process_speech(text):
    text_label.config(text=f"You said: {text}")
    words = text.strip().split()
    for word in words:
        handle_word(word)
    root.after(20000, reset_ui)

# ---------------- MICROPHONE LISTENING ----------------
def listen_microphone():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    try:
        # Uncomment this to see available microphones
        # print(sr.Microphone.list_microphone_names())

        with sr.Microphone() as source:
            root.after(0, lambda: text_label.config(text="Listening..."))
            root.after(0, lambda: video_label.config(text='', image=''))

            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Speak now...")

            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print("Audio captured")

            text = recognizer.recognize_google(audio)
            print("Recognized:", text)

            root.after(0, lambda: process_speech(text))

    except sr.UnknownValueError:
        print("Could not understand audio")
        root.after(0, lambda: text_label.config(text="Sorry, could not understand."))
    except sr.WaitTimeoutError:
        print("Listening timed out")
        root.after(0, lambda: text_label.config(text="Listening timed out."))
    except sr.RequestError as e:
        print("Google Speech API error:", e)
        root.after(0, lambda: text_label.config(text="Internet/API error. Check connection."))
    except OSError as e:
        print("Microphone error:", e)
        root.after(0, lambda: text_label.config(text=f"Mic error: {e}"))
    except Exception as e:
        print("General error:", e)
        root.after(0, lambda: text_label.config(text=f"Error: {e}"))

# ---------------- BUTTON ----------------
def on_mic_click():
    threading.Thread(target=listen_microphone, daemon=True).start()

mic_button = tk.Button(
    left_inner_frame,
    text="🎤 Mic",
    font=("Arial", 16),
    bg="#1E90FF",
    fg="white",
    width=10,
    height=2,
    command=on_mic_click
)
mic_button.pack(pady=20)

# ---------------- RESET UI ----------------
def reset_ui():
    video_label.config(image="", text="Welcome to Voice to ISL Translator")
    text_label.config(text="Click Mic to Speak")

# ---------------- START GUI ----------------
root.mainloop()