import tkinter as tk
from tkinter import messagebox
import create_narration as Narration


def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("TTS Narration Application")

    # Create a text input field
    input_text = tk.Text(root, height=10, width=40)
    input_text.pack()

    # Create a button to trigger narration creation
    create_button = tk.Button(root, text="Create Narration", command=lambda:Narration.create_narration(input_text))
    create_button.pack()
    return root

def main():
    root = create_gui()
    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
  main()
