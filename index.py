import speech_recognition as sr
import re
import pyttsx3

nome = ""

while(True):

    mic = sr.Recognizer()

    with sr.Microphone() as source:

        engine = pyttsx3.init()
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
        mic.adjust_for_ambient_noise(source)

        print("Vamos começar, fale algo...")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt-BR')

            if (re.search(r'\b' + "ajudar" + r'\b', format(frase))):
                engine.say("Ajuda");
                engine.runAndWait()
                print("Algo relacionado a ajuda.")

            elif (re.search(r'\b' + "Meu nome é " + r'\b', format(frase))):
                t = re.search('Meu nome é (.*)', format(frase))
                nome = t.group(1)
                print("Seu nome é " + nome)
                engine.say("Nome falado foi " + nome);
                engine.runAndWait()

            print("Voce falou: " + frase)

        except sr.UnknownValueError:
            print("Algo deu errado")