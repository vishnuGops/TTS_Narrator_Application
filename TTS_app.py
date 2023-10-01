import tkinter as tk
from tkinter import ttk
from tkinter import font
import create_narration as Narration


def create_gui():
    # init
    TTS = tk.Tk()
    TTS.title("TTS Narration Application")
    TTS.geometry("1080x680")
    TTS.configure(bg="grey")

    # App title
    heading_label = tk.Label(
        TTS, text="TTS Narration Application", fg="white", bg="grey", font=("Times", 20, "bold"))
    heading_label.pack()

    # Text input for tile title
    file_title = tk.Text(
        TTS, height=2, width=30,  font=("Times", 14))
    file_title.pack(pady=10)

    # Text input field for TTS conversion
    input_text = tk.Text(TTS, height=20, width=100,
                         font=("Times", 14))
    input_text.pack(pady=10)

    # Button to generate narration
    button_font = font.Font(family="Times", size=12, weight="bold")
    button_style = ttk.Style()
    button_style.configure("RoundedButton.TButton", borderwidth=15, font=button_font, height=3, width=20,
                           relief="raised", padding=10, borderround=20)
    geneate_narration_button = ttk.Button(TTS, style="RoundedButton.TButton", text="Create Narration",
                                          command=lambda: Narration.create_narration(input_text, file_title))
    geneate_narration_button.pack(pady=10)

    return TTS


def main():
    root = create_gui()
    # Run the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
