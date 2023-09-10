from googletrans import Translator
from gtts import gTTS
import keyboard
# import argparse
import os
while True:
    translator = Translator()

    userInput = input("Enter your text: ")

    translation = translator.translate(userInput)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

    audio = gTTS(text=translation.text, lang='en', slow=False)

    audio.save("translationOne.mp3")
    os.system("start translationOne.mp3")

    if keyboard.read_key() == "0":
        print("You pressed exit")
        break
