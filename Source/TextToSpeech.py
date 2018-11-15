import time
import espeak
import ntpath
import urllib.request as urlReq
from suds.client import Client as TTSClient
sounds_path = "/~/sounds/"


class Const:
    reqInterval = 0.5
    queryLimit = 10
    ttsClient = None # TTSClient("http://tts.itri.org.tw/TTSService/Soap_1_3.php?wsdl")
    account = "your_TTS_account"
    password = "your_TTS_PWD"
    transSucc = "0"
    queueSucc = "2"

class ITRI_TTS:
    # Getting back sound file which on ITRI remote server and store it on local.
    def getRemoteSoundFile(self, ttsID, count):
        # print("genRemoteSoundFile count:" + str(count))
        if(count > Const.queryLimit):
            return None

        ret = self.ttsClient.service.GetConvertStatus(Const.account, Const.password, ttsID)
        statRet = ret.split("&")
        # print(statRet)

        if statRet[2] == Const.queueSucc:
            print("URL:" + statRet[4])
            return statRet[4]
        else:
            print("Waitting for TTS Server...")

        time.sleep(Const.reqInterval)
        return self.genRemoteSoundFile(ttsID, count + 1)


    # Sending text to ITRI TTS web service
    def doTTS(self, textContent):
        if Const.ttsClient is None:
            Const.ttsClient = TTSClient("http://tts.itri.org.tw/TTSService/Soap_1_3.php?wsdl")
        
        # ret = ttsClient.service.ConvertSimple(account, password, textContent)
        # ret = ttsClient.service.ConvertText(account, password, textContent, "MCHEN_Joddess", 100, 1, "wav")
        #ConvertAdvancedText(account, password, textContent, "MCHEN_Joddess", 100, -6, "wav", 4, 0, 5)
        ret = self.ttsClient.service.ConvertAdvancedText(
            Const.account, Const.password, Const.textContent, "MCHEN_Joddess", 100, -6, "wav", 4, 0, 5)

        statRet = ret.split("&")
        if statRet[0] == Const.transSucc:
            path = self.getRemoteSoundFile(statRet[2], 0)
            wav_file_name = ntpath.basename(path)
            urlReq.urlretrieve(path, sounds_path + wav_file_name)
            return wav_file_name

        print("TTS Failed.")
        return None


class eSpeakTTS:
    def doTTS(self, textContent):
        es = espeak.ESpeak()
        es.voice = 'en+f4'
        es.speed = 100
        es.capitals = 25
        file_name = "{}_{}.wav".format(textContent, format(time.time(), ".0f"))
        full_file_path = "{}{}".format(sounds_path, file_name)
        es.save(textContent, full_file_path)
        print("save file name:{}".format(full_file_path))

        return file_name