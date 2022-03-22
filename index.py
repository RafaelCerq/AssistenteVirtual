import speech_recognition as sr
import re

nome = ""

while(True):

    mic = sr.Recognizer()

    with sr.Microphone() as source:

        mic.adjust_for_ambient_noise(source)

        print("Vamos começar, fale algo...")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt-BR')

            if (re.search(r'\b' + "ajudar" + r'\b', format(frase))):
                print("Algo relacionado a ajuda.")

            elif (re.search(r'\b' + "Meu nome é " + r'\b', format(frase))):
                t = re.search('Meu nome é (.*)', format(frase))
                nome = t.group(1)
                print("Seu nome é " + nome)

            print("Voce falou: " + frase)

        except sr.UnknownValueError:
            print("Algo deu errado")