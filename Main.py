from tkinter import *
from pynput.keyboard import Controller
import os
import threading
import speech_recognition as sr
from playsound import playsound
from datetime import datetime
from gtts import gTTS
from IPython.display import Audio

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
                print("음성을 기록합니다.")
                listener.adjust_for_ambient_noise(raw_voice)

                listener.dynamic_energy_adjustment_damping=0.2
                listener.pause_threshold = 0.6
                listener.energy_threshold = 600

                img_frm.config(image=mic1_img)

                print("음성을 입력합니다.")
                audio = listener.listen(raw_voice)

                img_frm.config(image=mic2_img)

                voice_data = listener.recognize_google(audio, language='ko')

            except UnboundLocalError:
                pass

            except sr.UnknownValueError:
                print("could not understand audio")
                return False

            if voice_data == "보이스":
                return playsound('sample.wav')
            if voice_data == "시간알려줘":
                now = datetime.now()
                time = gTTS("현재 시간은" + now.hour + "시" + now.minute + "분" + now.second + "초 입니다")
                time.save('time.wav')
                return display(Audio('time.wav', autoplay=True))

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