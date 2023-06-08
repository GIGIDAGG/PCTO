import cv2
import tkinter 
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

def seleziona_video():
    file_path = filedialog.askopenfilename(filetypes=[("File video", "*.mp4; *.avi")])
    return file_path

def seleziona_cartella():
    cartella = filedialog.askdirectory()
    return cartella

video_path = seleziona_video()

video = cv2.VideoCapture(video_path)
i = 0 #contatore screenshots
frames = []
j = 0 #contatore frames video capture

while video.isOpened():
    if video.grab():
        flag, frame = video.retrieve()
        if not flag:
            continue
        else:
            frame = cv2.resize(frame, (1920, 1080))
            frames.append(frame)
    else:
        break
cv2.imshow('video', frames[0])

while True:
    key = cv2.waitKey(10)
    if key == 100:
        if j < len(frames)-1:
            j = j + 1
            cv2.imshow('video', frames[j])
    if key == 97:
        if j > 0:
            j = j - 1
            cv2.imshow('video', frames[j])
        else:
            continue
    if key == 32:
        if i == 0:
            frame_path = seleziona_cartella()
        fourK = cv2.resize(frames[j], (3840, 2160))
        cv2.imwrite(frame_path+'/frame'+str(i+1)+'.png', fourK)
        i = i + 1
    if key == 13:
        key = 0
        while True:
            if j < len(frames)-1:
                key = cv2.waitKey(10)
                j = j + 1
                cv2.imshow('video', frames[j])
                if key == 13:
                    break
            else:
                break
    if key == 8:
        key = 0
        while True:
            if j > 0:
                key = cv2.waitKey(10)
                j = j - 1
                cv2.imshow('video', frames[j])
                if key == 8:
                    break
            else:
                break
    if key == 27:
        break

video.release()
