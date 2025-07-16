import streamlit as st
from main import *

st.title("AI Alphabet Teacher 👶🎤")
st.image(image_url, caption=f"{word}", width=200)
if st.button("Say the Word"):
    record_audio("child_audio.wav")
    score = check_pronunciation(word, "child_audio.wav")
    if score > 80:
        st.success("Great Job! ✅")
        speak("Great job!")
    else:
        st.error("Try Again! ❌")
        speak(f"Try again! It's pronounced {word}")
