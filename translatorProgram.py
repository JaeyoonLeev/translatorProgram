from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import googletrans
import tkinter.font

translator = googletrans.Translator()

##함수설정
def btnTranslateClick(): #번역시작
    try:
        text = beforeText.get(1.0, "end-1c")
        result1 = translator.translate(text, dest='en', src='auto')
        afterText.delete(1.0, "end-1c")
        afterText.insert(1.0, result1.text)
    except Exception as e:
        print("Error: ", e)

def btnTranslateSoundClick(): #소리재생
    try:
        readText = afterText.get(1.0, "end-1c")
        tts = gTTS(readText, lang='en')
        tts.save("completed.mp3")
        playsound("completed.mp3")
        os.remove("completed.mp3")
    except Exception as e:
        print("Error: ", e)   

def btnDeleteClick(): #내용지우기
    try:
        beforeText.delete(1.0, "end-1c")
        afterText.delete(1.0, "end-1c")
    except Exception as e:
        print("Error: ", e)           


##tkinter설정
##Widget설정

window=tkinter.Tk() # 윈도우 생성
window.title("영어 번역기") #윈도우 제목
window.geometry("600x240+800+300") #윈도우 크기 지정
window.resizable(True, True) #리사이즈 O, 크기조절 O

btnTranslate = tkinter.Button(window, 
                        overrelief="solid",
                        text="번역하기", 
                        width=15, 
                        command=btnTranslateClick, 
                        repeatdelay=1000, 
                        repeatinterval=100)

btnTranslateSound = tkinter.Button(window, 
                        overrelief="solid",
                        text="번역내용 듣기", 
                        width=15, 
                        command=btnTranslateSoundClick, 
                        repeatdelay=1000, 
                        repeatinterval=100)

btnDelete = tkinter.Button(window, 
                        overrelief="solid",
                        text="내용 지우기", 
                        width=15, 
                        command=btnDeleteClick, 
                        repeatdelay=1000, 
                        repeatinterval=100)

##붙이기
beforeText = Text(width = 30, height = 10)
beforeText.grid(row=2, column=1, padx=10, pady=10)

afterText = Text(width = 30, height = 10)
afterText.grid(row=2, column=3, padx=10, pady=10)

btnTranslate.grid(row=3, column=1, padx=10, pady=10)
btnTranslateSound.grid(row=3, column=3, padx=10, pady=10)
btnDelete.grid(row=4, column=2, padx= 10, pady = 10)

#실행
window.mainloop()
