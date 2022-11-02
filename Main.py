from tkinter import *
from pynput.keyboard import Controller
import os
import threading
import requests
import speech_recognition as sr
from playsound import playsound
import json

apikey = "8acd32db4d29ff5cb142deafb9fd1152"
city = "Seoul"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}"
result = requests.get(api)
data = json.loads(result.text)
class voiceloop(threading.Thread):

    mykeyboard = Controller()

    def run(self) -> None:

        while True:
            voice = self.CollectVoice()

            if voice != False and myThread.rflag == True:
                print(voice)
                self.Pasting(voice)

            if myThread.rflag == False:
                break

    def Pasting(self, myvoice):
        for character in myvoice:
            self.mykeyboard.type(character)
        self.mykeyboard.type(" ")

    def CollectVoice(self):
        listener = sr.Recognizer()
        voice_data = ""

        with sr.Microphone() as raw_voice:

            try:
                img_frm.config(image=mic3_img)
                print("잠시만 기다려주세요")
                listener.adjust_for_ambient_noise(raw_voice)

                listener.dynamic_energy_adjustment_damping=0.2
                listener.pause_threshold = 0.6
                listener.energy_threshold = 600

                img_frm.config(image=mic1_img)

                print("목소리를 수집합니다...")
                audio = listener.listen(raw_voice)

                img_frm.config(image=mic2_img)

                voice_data = listener.recognize_google(audio, language='ko')

            except UnboundLocalError:
                pass

            except sr.UnknownValueError:
                print("소리를 인식하기 힘듭니다.")
                return False

            if voice_data == "안녕":
                playsound('Main.wav')
                return False

            if voice_data == "날씨" or "오늘의 날씨":
                if data["weather"][0]["description"] == "맑음":
                    print("날씨는 ",data["weather"][0]["description"],"입니다.")
                    playsound('clear.wav')
                return False


            return str(voice_data)


def on_closing():
    myThread.rflag=False
    print("finish work")
    os._exit(1)


root = Tk()
root.title("Voice catcher")
root.geometry("200x200+50+50")

mic1_img = PhotoImage(file="mic1.png")
mic2_img = PhotoImage(file="mic2.png")
mic3_img = PhotoImage(file="mic3.png")

img_frm = Label(root, image=mic2_img)
img_frm.pack();

myThread = voiceloop()
myThread.rflag = True
myThread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.wm_attributes("-topmost",1)
root.mainloop()