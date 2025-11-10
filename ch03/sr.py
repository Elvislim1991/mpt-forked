import speech_recognition as sr

speech = sr.Recognizer()

# List available microphones
print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"  {index}: {name}")

print("\nPython is listening (using pulse for Bluetooth support)...")

# Use pulse device (index 4) to access Bluetooth devices like AirPods
with sr.Microphone(device_index=5) as source:
    print(f"Using microphone: {sr.Microphone.list_microphone_names()[5]}")
    speech.adjust_for_ambient_noise(source)
    speech.energy_threshold = 300
    speech.dynamic_energy_threshold = True
    print("Listening... speak now!")
    audio = speech.listen(source, phrase_time_limit=5, timeout=10)

try:
    inp = speech.recognize_google(audio)
    print(f"You just said {inp}.")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Error with the recognition service: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
