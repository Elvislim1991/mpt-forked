import speech_recognition as sr
# from mysr import voice_to_text
import os
import wave
from datetime import datetime

speech = sr.Recognizer()
os.environ['PULSE_SOURCE'] = 'bluez_input.50:F3:51:BD:F2:32'
# List available microphones
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"  {index}: {name}")

while True:
    print("Python is listening...")
    inp = ""
    with sr.Microphone(device_index=5) as source:
        # speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            
            # Save audio for troubleshooting
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"captured_audio_{timestamp}.wav"
            with open(filename, "wb") as f:
                f.write(audio.get_wav_data())
            print(f"Audio saved as {filename}")

            print("Recognizing...")
            inp = speech.recognize_google(audio)
            print("return from google")
        except sr.UnknownValueError:
            print("Could not understand audio")
            pass
        except sr.RequestError:
            print("Network error")
            pass
        except sr.WaitTimeoutError:
            print("Timeout error")
            pass
    print(f"You just said {inp}.")
    if inp.lower() == "stop listening":
        print("Goodbye!")
        break
