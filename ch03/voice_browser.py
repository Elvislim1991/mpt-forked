import webbrowser

import speech_recognition as sr

speech = sr.Recognizer()

# List available microphones
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"  {index}: {name}")


def voice_to_text():
    voice_input = ""
    with sr.Microphone(device_index=3) as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error")
        except sr.WaitTimeoutError:
            pass
    return voice_input


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
