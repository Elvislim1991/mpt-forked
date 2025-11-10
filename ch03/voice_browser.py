import webbrowser

import speech_recognition as sr
from mysr import voice_to_text

speech = sr.Recognizer()

# List available microphones
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"  {index}: {name}")


while True:
    print("Python is listening...")
    inp = voice_to_text()
    print(f"You just said {inp}.")
    if inp == "stop listening":
        print("Goodbye!")
        break
    elif "browser" in inp:
        inp = inp.replace("browser ", "")
        webbrowser.open("http://" + inp)
        continue
