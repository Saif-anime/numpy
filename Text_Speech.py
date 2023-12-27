import pygame
from gtts import gTTS
# Text you want to convert to speechissss
text= "Hi Anaksha. How are you?"

# Initialize the gTTS object with the text
tts = gTTS(text, lang='hi')



# Save the generated speech as an audio file (e.g., mp3)
tts.save("short4.mp3")

# Initialize pygame mixer

pygame.mixer.init()

# Load and play the generated audio
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

# Wait for the audio to finish playing
# pygame.time.wait(int(tts.duration * 1000))  # Convert duration to milliseconds
