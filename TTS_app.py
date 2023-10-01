import tkinter as tk
from tkinter import font
import create_narration as Narration


def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("TTS Narration Application")

    # Set the initial window size to 960x540
    root.geometry("960x540")
    root.configure(bg="white")

    # Create a label for the heading title
    heading_label = tk.Label(
        root, text="TTS Narration Application", font=("Arial", 20))
    heading_label.pack()

    # Create a text input field
    input_text = tk.Text(root, height=20, width=100)
    input_text.pack()

    custom_font = font.Font(family="Arial", size=12, weight="bold")
    # Create a button to trigger narration creation
    create_button = tk.Button(root, height=3, width=30, text="Create Narration", font=custom_font,
                              bg="#9E9E9E", fg="white", command=lambda: Narration.create_narration(input_text))
    create_button.pack()
    return root


def main():
    root = create_gui()
    # Run the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
