from tkinter import Button, Label, Tk
from tkinter.ttk import Combobox


class Gui(Tk):
    def __init__(self, *args, **kwargs):
        super.__init__(self, *args, **kwargs)
        self.title("PES Audio to Text")
        w = 600 # width for the Tk root
        h = 530 # height for the Tk root
        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.source_language_combo_box = Combobox(self, text="Source language", values=source_languages_list)
        self.source_language_combo_box.set(0)
        self.translation_language_combo_box = Combobox(self, text="Translation language", values=source_languages_list)
        self.translation_language_combo_box.set(0)
        self.select_source_folder = Button(self, text="Select folder with wav files",command=None)
        self.start_button = Button(self, text="Translate/Transcribe", command=None)


        
source_languages_list = [
    "Japanese",
    "Korean", 
    "English (GB)",
    "English (US)", 
    "Spanish (Spain)", 
    "Spanish (Mexico)", 
    "Italian",
    "French", 
    "Polish", 
    "Portuguese (PT)", 
    "Portuguese (BR)", 
    "German", 
    "Russian", 
]

languages_code_list = [
    "ja", 
    "ko", 
    "en-GB", 
    "en-US",
    "es-ES",
    "es-MX",
    "it-IT",
    "fr-FR",
    "pl",
    "pt-PT",
    "pt-BR",
    "de-DE",
    "ru",
]
