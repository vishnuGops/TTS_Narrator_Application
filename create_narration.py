import tkinter as tk
from gtts import gTTS
from tkinter import messagebox

# Function to create a narration
def create_narration(input_text):
    text = input_text.get("1.0", "end-1c")  # Get the text from the input field
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            messagebox.showinfo("Success", "Narration created and saved as 'output.mp3'")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")