from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

with open("medium.txt", "r") as newReadUsingWithContext:
    text = newReadUsingWithContext.read()

translation = translator.translate(text)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

audio = gTTS(text=translation.text, lang='en', slow=False)

audio.save("translationOne.mp3")
os.system("start translationOne.mp3")
