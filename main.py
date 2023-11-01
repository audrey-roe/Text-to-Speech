from pdfminer.high_level import extract_text
import pyttsx3
import re
from module.text_extractor import format_text
from module.text_speech_converter import TextToSpeech

text = extract_text("./Book_input/Americanah.pdf")

cleaned_text = format_text(text=text)

tts = TextToSpeech(rate=200, volume=1.0)
# tts.list_available_voices()
tts.text_to_speech(cleaned_text, save=True, file_name="test.mp3")