import speech_recognition as sr

def record_audio(filename="child_audio.wav"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
