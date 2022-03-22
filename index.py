import speech_recognition as sr
import re

while(True):

    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        print("Vamos começar, fale algo..")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt-br')

            if (re.search(r'\b' + "ajudar" + r'\b', format(frase))):
                print("algo relacionado a ajuda.")


            print('Você falou: ' + frase)

        except sr.UnknownValueError:
            print("Algo deu errado")