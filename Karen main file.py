from datetime import datetime
import speech_recognition as sr
# "pyttsx3 is a text-speech library"
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#Configure browser
# set the path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))
#speech engine initialsation (pyttsx3)

Engine = pyttsx3.init() # object creation

#""" RATE"""

rate = Engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate

#"""VOLUME"""

volume = Engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
Engine.setProperty('volume',0.5)    # setting up volume level  between 0 and 1


Voice = Engine.getProperty('voices')
Engine.setProperty('voice',Voice[1].id) # 0 = male , 1 = female
ActivationWord = "Karen" # single word


#"""Saving Voice to a file"""
Engine.save_to_file('Hello World', 'test.mp3')
Engine.runAndWait()



def speak(text,rate = 125): #set speaking rate voice
    Engine.setProperty('rate',rate)
    if text  == 'all system nominal.':
        Engine.say("Hello Miss, this is karen")

    elif text == 'greeting':
        Engine.say()

    else: Engine.say(text)

    Engine.runAndWait()
    
    
def PersonCommand():
    listener = sr.Recognizer()
    print(" Listening For a Command . . . . ")
    
    with sr.Microphone() as source :
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recogniza speech')
        Quary = listener.recognize_google(input_speech, language ='en_gb')
        print(f'the input speech was:{Quary}')
        

    except Exception as exception:
        print('i did not catch that')
        speak('i did not catch that')
        print (exception)
        return 'None'
    return Quary

def search_wikipedia(Quary = ''):
    searchRes = wikipedia.search(Quary)
    if not searchRes:
        print('No wikipedia Result')
        return 'No result recived'
    try:
        wikipage = wikipedia.page(searchRes[0])
    except wikipedia.DisambiguationError as error:
        wikipage = wikipedia.page(error.option[0])
    print(wikipage.title)
    wikisummery = str(wikipage.summary)
    return wikisummery


def analysis(given):
    pass



#main Loop
if __name__ == '__main__':
    speak('all system nominal.')

    while True:
        Quary = PersonCommand().split()
        if Quary[0] == 'Close':
            break

        if Quary[0] == ActivationWord:
            Quary.pop(0)
            
            #list commaands
            if Quary[0] == 'say':
                if 'hello' in Quary:
                    speak('greeting,all.')
                else:
                    Quary.pop(0)
                    speech = ' '.join(Quary)
                    speak(speech)       
            #navigation
            if Quary[0] == 'go' and Quary[1] == 'to':
                speak('opening . . .')
                Quary = ' '.join (Quary[2:])
                webbrowser.get('chrome').open_new(Quary)
            
            #wikipedia
            if Quary[0] == 'wikipedia':
                Quary = ' '.join(Quary[1:])
                speak('Qquarying the universal databacnk')
                search_wikipedia(Quary[1:])
