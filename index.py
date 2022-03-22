import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)

    print("Vamos começar")

    audio = mic.listen(source)

    try:
        frase = mic.recognize_google(audio, language='pt-br')
        print('Você falou: ' + frase)

    except sr.UnknownValueError:
        print("Algo deu errado")