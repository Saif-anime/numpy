import pygame
from gtts import gTTS

# Text you want to convert to speechissss
text = "Kya Aap Jaante hai ki World Wide Web ka Invention kisne kiya hai. Chaliya Aapko batate hai ki HTML ko banane wale Sir Tim Berners-Lee hai. joh ki Ek British Computer Scientist The 1990s mein voh kaam karte the C.E.R.N mein. vaha per crucial development karte samaye unhone World Wide Web ka Invention kiya tha."

# Initialize the gTTS object with the text
tts = gTTS(text, lang='hi')

# Save the generated speech as an audio file (e.g., mp3)
tts.save("short1.mp3")

# Initialize pygame mixer

pygame.mixer.init()

# Load and play the generated audio
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

# Wait for the audio to finish playing
# pygame.time.wait(int(tts.duration * 1000))  # Convert duration to milliseconds
