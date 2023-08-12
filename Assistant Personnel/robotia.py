import speech_recognition as sr
import pyttsx3 as ptx
import pywhatkit
import datetime #Pour lavoir accès à l'heure


#on permet l'utilisation du micro afin qu'ol ecoute et on initialise la voix
listener= sr.Recognizer()   
engine = ptx.init() #pour initialiser la voix
voice = engine.getProperty("voices") 
engine.setProperty("voice","french")  #on change la langue en francais

#la fonction qui va nous permettre de declencher la conversation
def parler(text):
    engine.say(text) #le texte qu'on va prononcer
    engine.runAndWait()  #pour qu'il écoute

def ecouter():
    try:
        with sr.Microphone() as source :  #avec le micro ouvert il va ouvrir un fichier
            print("parler")
            voix=listener.listen(source)  #quand on va parler on va lui demander d'ecouter
            command = listener.recognize_google(voix, language='fr-FR')
    except:
        pass
    return command

def communiquer():
    command = ecouter()
    print(command)
    if 'bonjour' in command:
        parler('bonjour comment allez vous ?')
    elif 'oui ca va et toi' in command:
        parler('oui ca va de mon côté, comment puis je vous aider ?')
    
    elif 'Mettez la chanson de ' in command:
        chanteur=command.replace('Mettez la chanson de')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parler("il est :" +heure)
    elif 'ton nom' in command:
        parler("Je m'appelle  Daniel")

while True:
    communiquer()