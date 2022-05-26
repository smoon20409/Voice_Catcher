from tkinter import *
from pynput.keyboard import Controller
import os
import threading
import speech_recognition as sr

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
                print("기다리시고")
                listener.adjust_for_ambient_noise(raw_voice)

                listener.dynamic_energy_adjustment_damping=0.2
                listener.pause_threshold = 0.6
                listener.energy_threshold = 600

                img_frm.config(image=mic1_img)

                print("말하세요!")
                audio = listener.listen(raw_voice)

                img_frm.config(image=mic2_img)

                voice_data = listener.recognize_google(audio, language='ko')

            except UnboundLocalError:
                pass

            except sr.UnknownValueError:
                print("could not understand audio")
                return False

            if voice_data == "보이스":
                return str('네 보이스 입니다.')


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