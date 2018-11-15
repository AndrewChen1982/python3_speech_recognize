import traceback
import time
import speech_recognition as sr

isRunning = True
content = ""
recognizer = None

class ColorTags:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

g_custom_callback = lambda: None

def initRecognizer(custom_callback):
    global g_custom_callback
    if custom_callback is not None:
        g_custom_callback = custom_callback
    
    # recognize speech using Google Speech Recognition
    global recognizer
    recognizer = sr.Recognizer()

def startRecognize():
    try:
        with sr.Microphone(device_index=2) as source:
            print("\n" + ColorTags.OKGREEN + 
                "*** Waitting for speech ***\n" +
                ColorTags.ENDC)

            global recognizer
            recognizer.adjust_for_ambient_noise(source)                            
            
            listen_callback(recognizer.listen(source, timeout = 10))
        
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `re.recognize_google(audio)`
        
        # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
         
    except:
        traceback.print_exc()
        print("Something Wrong")

    print("End Recognizing")


def listen_callback(audio):
    try:
        global content
        global recognizer
        content = recognizer.recognize_google(audio)
        # content = recognizer.recognize_wit(audio, key="6HSYD74MNWI5TFY6G72V6OF2GDM6APZL")
        
        print("Google Speech Recognized: " + content)

        global g_custom_callback
        g_custom_callback(content)
        
        # global isRunning
        # isRunning = False

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except:
        traceback.print_exc()
        print("Something Wrong")

def getRecognizeContent():
    global content
    return content

