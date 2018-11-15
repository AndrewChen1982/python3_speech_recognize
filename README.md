# python3_speech_recognize

## Google speech recognition and ITRI(工研院) / espeak text to speech(TTS) in python3

## 1. Google speech recognition:
### Step:
1. Install python package "traceback", "time", "speech_recognition".
    * I use apt for installing package: "sudo apt-get install traceback time speech_recognition -y".

2. Calling function initRecognizer(callback_function) **`only once`**.

3. Calling function startRecognize() at any time you like to do speech Recognition.

> Note: In function startRecognize, there is an argument "device_index"
> ```python
> with sr.Microphone(device_index=2) as source:
> ```
>
> "device_index" means your microphone's index on your computer. You should check it by running the following code:
> ```python
> import speech_recognition as sr
> for index, name in enumerate(sr.Microphone.list_microphone_names()):
>    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
> ```
>
> It will print out something like the following:
> ```python
> Microphone with name "HDA Intel HDMI: 0 (hw:0,3)" found for `Microphone(device_index=0)`
> Microphone with name "HDA Intel HDMI: 1 (hw:0,7)" found for `Microphone(device_index=1)`
> Microphone with name "HDA Intel HDMI: 2 (hw:0,8)" found for `Microphone(device_index=2)`
> Microphone with name "Blue Snowball: USB Audio (hw:1,0)" found for `Microphone(device_index=3)`
> Microphone with name "hdmi" found for `Microphone(device_index=4)`
> Microphone with name "pulse" found for `Microphone(device_index=5)`
> Microphone with name "default" found for `Microphone(device_index=6)`
> ```
> `Microphone with name "Blue Snowball: USB Audio (hw:1,0)" found for Microphone(device_index=3)` might be you really want to use, so that your device_index should set be 3.

## 2. Text to speech by ITRI or espeak:
## Setp:
1. Install python package "traceback", "time", "espeak", "ntpath", "urllib" ,"suds".
    * I use apt for installing package: "sudo apt-get install time espeak ntpath urllib suds -y".

2. Calling function "doTTS" from class ITRI_TTS or eSpeakTTS with text as parameter.
    * If you try to use ITRI tts, you need to register to ITRI to get account and password for using ITRI's web service. [ITRI TTS](http://tts.itri.org.tw/ "http://tts.itri.org.tw/")    

3. Function "doTTS" will generate a wave file and retun file name.

4. Just play out wave file, you will hear the voice's content as the same text you put in.

## end
