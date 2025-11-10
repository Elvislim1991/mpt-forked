from datetime import datetime
import platform
import speech_recognition as sr

if platform.system() == "Linux":
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll

    # Define error handler
    error_handler = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

    # Don't do anything if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
        pass

    # Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary("libasound.so")
    asound.snd_lib_error_set_handler(c_error_handler)

speech = sr.Recognizer()


# Now define the voice_to_text() function for all platforms
def voice_to_text(troubleshoot=False):
    voice_input = ""
    with sr.Microphone(device_index=5) as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            if troubleshoot:
                # Save audio for troubleshooting
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"captured_audio_{timestamp}.wav"
                with open(filename, "wb") as f:
                    f.write(audio.get_wav_data())
                print(f"Audio saved as {filename}")
            print("Recognizing...")
            voice_input = speech.recognize_google(audio)
            print("return from google")
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Network error")
        except sr.WaitTimeoutError:
            print("Waiting for input...")
    return voice_input


if __name__ == "__main__":
    print(voice_to_text())
