#Python 2.x program for Speech Recognition 

import speech_recognition as sr 
from playsound import playsound
from gtts import gTTS
import os


def func1():
        #enter the name of usb microphone that you found 
        #using lsusb 
        #the following name is only used as an example 
        mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
        #Sample rate is how often values are recorded 
        sample_rate = 48000
        #Chunk is like a buffer. It stores 2048 samples (bytes of data) 
        #here. 
        #it is advisable to use powers of 2 such as 1024 or 2048 
        chunk_size = 2048
        #Initialize the recognizer 
        r = sr.Recognizer() 

        #generate a list of all audio cards/microphones 
        mic_list = sr.Microphone.list_microphone_names() 

        device_id=0
        #the following loop aims to set the device ID of the mic that 
        #we specifically want to use to avoid ambiguity.


        for i, microphone_name in enumerate(mic_list): 
                if microphone_name == mic_name: 
                        device_id = i 

        #use the microphone as source for input. Here, we also specify 
        #which device ID to specifically look for incase the microphone 
        #is not working, an error will pop up saying "device_id undefined" 
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source: 
                #wait for a second to let the recognizer adjust the 
                #energy threshold based on the surrounding noise level 
                r.adjust_for_ambient_noise(source) 
                print ("Say Something")
                #listens for the user's input 
                audio = r.listen(source)

                        
                try: 
                        text = r.recognize_google(audio) 
                        return text
                        mytext=text
                        language='en'
                        myobj = gTTS(text=mytext, lang=language, slow=False)
                        myobj.save("welcome.mp3")

                        #playsound('welcome.mp3')
                        #os.system("mpg321 welcome.mp3")'''
                        
          
                
                except sr.UnknownValueError: 		return("Google Speech Recognition could not understand audio") 
                
                except sr.RequestError as e: return("Could not request results from Google Speech Recognition service; {0}".format(e))


