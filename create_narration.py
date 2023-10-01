import tkinter as tk
from gtts import gTTS
from tkinter import messagebox
import TTS_app as app
import datetime
import os


def create_narration(input_text, title):
    text = input_text.get("1.0", "end-1c")  # Get the text from the input field
    title_text = title.get("1.0", "end-1c")
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            dateTime = str(
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
            file_title = f"{title_text}-{dateTime}"
            save_narration(tts, file_title)
            messagebox.showinfo(
                "Success", "Narration created and saved as '" + file_title + ".mp3'")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")


def save_narration(tts, title):
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    file_title = os.path.join(output_folder, title + ".mp3")
    tts.save(file_title)
