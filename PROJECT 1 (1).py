import speech_recognition as sr
from googletrans import Translator

# Function to recognize speech using Google Speech Recognition
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Function to translate text using Google Translate API
def translate_text(text, dest_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text
def translate_text(text, dest_lang='te'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

if __name__ == "__main__":
    # Recognize speech
    recognized_text = recognize_speech()
    if recognized_text:
        print(f"Recognized Speech: {recognized_text}")

        # Translate recognized text (e.g., translate to Spanish 'es')
        translated_text = translate_text(recognized_text, dest_lang='te')
        print(f"Translated Text: {translated_text}")
        translated_text = translate_text(recognized_text, dest_lang='en')
        print(f"Translated Text: {translated_text}")
