import pyttsx3
from transformers import pipeline

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load a text generation model
text_generator = pipeline("text-generation", model="gpt2")

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()
    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1)     # Volume 0-1

    # List all available voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # You can choose a different voice from the list


if __name__ == "__main__":
    print("Welcome to your talking assistant! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            speak("Goodbye!")
            break

        # Generate a response using the text generation pipeline
        response = text_generator(user_input, max_length=50, num_return_sequences=1)
        answer = response[0]['generated_text']
        print(f"Bot: {answer}")
        speak(answer)

