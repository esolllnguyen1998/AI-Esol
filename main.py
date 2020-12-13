import pyttsx3

esol = pyttsx3.init()
voice = esol.getProperty('voices')
esol.setProperty('voice', voice[1].id)

def speak(audio):
    esol.say(audio)
    esol.runAndWait()

speak("Hello Yen Nhi Dien Khung")