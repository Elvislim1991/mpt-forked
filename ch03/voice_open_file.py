import os
import pathlib
import platform
import speech_recognition as sr
from mysr import voice_to_text

speech = sr.Recognizer()

directory = pathlib.Path.cwd()


def open_file(filename):
    if platform.system() == "Windows":
        os.system(f"explorer {directory}\\files\\{filename}")
    elif platform.system() == "Darwin":
        os.system(f"open {directory}/files/{filename}")
    else:
        os.system(f"xdg-open {directory}/files/{filename}")


while True:
    print("Python is listening...")
    inp = voice_to_text().lower()
    print(f"You just said {inp}.")
    if inp == "stop listening":
        print("Goodbye!")
        break
    elif "open pdf" in inp:
        inp = inp.replace("open pdf ", "")
        myfile = f"{inp}.pdf"
        open_file(myfile)
        continue
    elif "open word" in inp:
        inp = inp.replace("open word ", "")
        myfile = f"{inp}.docx"
        open_file(myfile)
        continue
    elif "open excel" in inp:
        inp = inp.replace("open excel ", "")
        myfile = f"{inp}.xlsx"
        open_file(myfile)
        continue
    elif "open text" in inp:
        inp = inp.replace("open text ", "")
        myfile = f"{inp}.txt"
        open_file(myfile)
        continue
    elif "open powerpoint" in inp:
        inp = inp.replace("open powerpoint ", "")
        myfile = f"{inp}.pptx"
        open_file(myfile)
        continue
    elif "open mp3" in inp:
        inp = inp.replace("open mp3 ", "")
        myfile = f"{inp}.mp3"
        open_file(myfile)
        continue
