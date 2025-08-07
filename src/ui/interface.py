# src/ui/interface.py

from tkinter import Tk, Label, Text, Button, StringVar, OptionMenu

class TranslationInterface:
    def __init__(self, master):
        self.master = master
        master.title("Language Translation Tool")

        self.label = Label(master, text="Enter text to translate:")
        self.label.pack()

        self.text_box = Text(master, height=10, width=50)
        self.text_box.pack()

        self.source_lang = StringVar(master)
        self.target_lang = StringVar(master)

        self.source_lang.set("Select Source Language")  # default value
        self.target_lang.set("Select Target Language")  # default value

        self.language_options = ["English", "Spanish", "French", "German", "Japanese"]  # Example languages

        self.source_dropdown = OptionMenu(master, self.source_lang, *self.language_options)
        self.source_dropdown.pack()

        self.target_dropdown = OptionMenu(master, self.target_lang, *self.language_options)
        self.target_dropdown.pack()

        self.translate_button = Button(master, text="Translate", command=self.translate_text)
        self.translate_button.pack()

    def translate_text(self):
        # Placeholder for translation logic
        input_text = self.text_box.get("1.0", "end-1c")
        source = self.source_lang.get()
        target = self.target_lang.get()
        # Call the translation function from translator.py here
        print(f"Translating '{input_text}' from {source} to {target}...")  # Replace with actual translation call

if __name__ == "__main__":
    root = Tk()
    translation_interface = TranslationInterface(root)
    root.mainloop()