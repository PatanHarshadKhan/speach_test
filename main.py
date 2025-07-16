from alphabet_data import alphabet_data
from generate_image import get_image_url
from recorder import record_audio
from tts import speak
from pronunciation_check import check_pronunciation

# Choose A for now
letter_data = alphabet_data[0]
word = letter_data["word"]
prompt = letter_data["prompt"]

# 1. Generate Image
image_url = get_image_url(prompt)
print("Image:", image_url)

# 2. Speak the word
speak(f"This is an {word}. Can you say {word}?")

# 3. Record the child's voice
record_audio("child_audio.wav")

# 4. Check Pronunciation
score = check_pronunciation(word, "child_audio.wav")
print("Score:", score)

# 5. Give Feedback
if score > 80:
    speak("Great Job!")
else:
    speak(f"Almost! It's pronounced {word}")
