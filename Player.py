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

if video_path:
    video = cv2.VideoCapture(video_path)
    i = 0 #contatore screenshots
    frames = []
    j = 0 #contatore frames video capture
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

def riproduci_video(avanti):
    global video, j, frames
    if avanti == True:
        if video.isOpened():
            flag, frame = video.read()
            if not flag:
                return 0
            else:
                frame = cv2.resize(frame, (1920, 1080))
                frames.append(frame)
    cv2.imshow('video', frames[j])
    return j

video_path = seleziona_video()
video = cv2.VideoCapture(video_path)
frames = []  # Array that contains the video frames
i = 0  # Counter for screenshots
j = 0  # Counter for video frames
riproduci_video(True)
while True:
    key = cv2.waitKey(10)
    if key == 100:
        j = riproduci_video(True)
    if key == 97:
        j = j - 1 if j > 0 else 0
        riproduci_video(False)
    if key == 32:
        if i == 0:
            frame_path = seleziona_cartella()
        fourK = cv2.resize(frames[j], (3840, 2160))
        cv2.imwrite(frame_path + '/frame' + str(i + 1) + '.png', fourK)
        i = i + 1
    if key == 13:
        while j < len(frames) - 1:
            key = cv2.waitKey(10)
            j = j + 1
            riproduci_video(True)
            if key == 13:
                break
    if key == 8:
        while j > 0:
            key = cv2.waitKey(10)
            j = j - 1
            riproduci_video(True)
            if key == 8:
                break
    if key == 27:
        break

    if video.grab():
            flag, frame = video.retrieve()
            if flag:
                frame = cv2.resize(frame, (1920, 1080))
                frames.append(frame)
                cv2.imshow('frame', frames[0])

    while True:
        key = cv2.waitKey(0)
        if key == 100:
            if video.grab():
                flag, frame = video.retrieve()
                if not flag:
                    continue
                else:
                    frame = cv2.resize(frame, (1920, 1080))
                    frames.append(frame)
                    j = j + 1
                    cv2.imshow('frame', frames[j])
        if key == 97:
            if j > 0:
                j = j - 1
                cv2.imshow('frame', frames[j])
            else:
                continue
        if key == 32:
            if i == 0:
                frame_path = seleziona_cartella()
            if frame_path:
                fourK = cv2.resize(frames[j], (3840, 2160))
                cv2.imwrite(frame_path+'/frame'+str(i+1)+'.png', fourK)
                i = i + 1
            else:
                print("Nessuna cartella selezionata.")
        if key == 27:
            break
else:
    print("Nessuna video selezionato.")

video.release()
video.release()
cv2.destroyAllWindows()
