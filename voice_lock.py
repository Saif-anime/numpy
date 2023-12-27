import speech_recognition as sr

def enroll_voiceprint(user_id, num_samples=3):
    # Collect and store voiceprints along with user identities
    # Implement voice enrollment logic here
    recognizer = sr.Recognizer()
    print(f"Collecting voice samples for user...")
    for i in range(num_samples):
        with sr.Microphone() as source:
            print(f"Sample {i + 1}: Speak now...")
            audio = recognizer.listen(source)

        # Save the audio as a file
        sample_filename = f"voice_samples/user_{user_id}_sample_{i}.wav"
        with open(sample_filename, "wb") as f:
            f.write(audio.get_wav_data())

        print(f"Sample {i + 1} saved as {sample_filename}")


def verify_speaker():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    # Convert the voice input to text
    recognized_text = recognizer.recognize_google(audio).lower()
    
    # Compare the recognized voiceprint with enrolled voiceprints
    if recognized_text == "your_enrolled_voiceprint":
        print("Speaker verified.")
    else:
        print("Speaker not verified. Access denied.")

# Enroll voiceprints (do this only once for each user)
enroll_voiceprint("Saif", num_samples=3)

# Verify the speaker's identity
verify_speaker()
