from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
from pygame import mixer
from gtts import gTTS
import os

def translate_and_play():
    string = text_entry.get()
    selected_language = selected_language_var.get()
    language_codes = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        # Add more languages as needed
    }
    tts = gTTS(text=string, lang=language_codes[selected_language], tld="com")
    out = "audio1"
    os.chdir(r"C:\Users\Don\Documents\pyscripts\audios")
    things = list(os.listdir())
    if things:
        latest_file = max(things, key=lambda x: int(x.split('.')[0][-1]))
        latest_number = int(latest_file.split('.')[0][-1])
        out = "audio" + str(latest_number + 1)
    tts.save(out + ".mp3")
    mixer.init()
    mixer.music.load(out + ".mp3")
    mixer.music.play()

# Create the GUI window
window = Tk()
window.title("Text to Audio Translator")

# Create GUI components
label_text = Label(window, text="Enter text to translate:")
label_text.pack()

text_entry = Entry(window)
text_entry.pack()

label_language = Label(window, text="Select language:")
label_language.pack()

available_languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    # Add more languages as needed
}

selected_language_var = StringVar(window)
selected_language_var.set("en")

language_selection = OptionMenu(window, selected_language_var, *available_languages.keys())
language_selection.pack()

translate_button = Button(window, text="Translate and Play", command=translate_and_play)
translate_button.pack()

# Run the GUI event loop
window.mainloop()
