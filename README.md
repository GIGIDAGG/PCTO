# Progetto per il riconoscimento delle boe nel mare utilizzando YOLOv5

## Introduzione
Questo progetto è orientato all'allenamento di un modello di machine learning per il riconoscimento delle boe nel mare. Il processo di sviluppo del progetto coinvolge l'utilizzo di Visual Studio per la realizzazione di un video player personalizzato che consente di scorrere il video avanti, indietro, stop e play. Successivamente, viene utilizzato Roboflow per la labellizzazione delle immagini, mentre Colab viene utilizzato per scrivere il codice utilizzando il framework YOLOv5 e il dataset COCO.

## Strumenti utilizzati
- Visual Studio: utilizzato per creare un video player personalizzato con funzionalità di avanzamento, retrocessione, stop e riproduzione.
- Roboflow: utilizzato per la labellizzazione delle immagini, cioè per annotare manualmente le boe nelle immagini del dataset.
- Colab: utilizzato per scrivere il codice utilizzando il framework YOLOv5 e il dataset COCO.
- YOLOv5: framework di deep learning utilizzato per l'addestramento del modello di riconoscimento delle boe.
- Dataset COCO: dataset di immagini ampiamente utilizzato per l'addestramento di modelli di riconoscimento oggetti.

## Raccolta dati
Per addestrare il modello di riconoscimento delle boe, è necessario raccogliere un ampio set di dati contenente video che mostrano boe nel mare. È importante acquisire sequenze di diversi tipi di boe, in diverse condizioni di illuminazione e di sfondo, al fine di rendere il modello più robusto e generale. Il dataset può essere arricchito con l'aggiunta di etichette che indicano la presenza o l'assenza di boe in ciascun frame del video.

## Codice Python utilizzato in Visual Studio - player
```python
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

    #1° metodo per ottenere i frame di video
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
            if frame_path:
                fourK = cv2.resize(frames[j], (3840, 2160))
                cv2.imwrite(frame_path+'/frame'+str(i+1)+'.png', fourK)
                i = i + 1
            else:
                print("Nessuna cartella selezionata.")
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
else:
    print("Nessuna video selezionato.")

video.release()
```

## Descrizione del codice del video player
Questo codice utilizza le librerie OpenCV e tkinter per creare un'applicazione che consente di selezionare un video, visualizzarlo e catturare i frame desiderati. Ecco una descrizione dettagliata del codice:

1. Importazione delle librerie: vengono importate le librerie OpenCV e tkinter.

2. Creazione di una finestra GUI: viene creato un oggetto Tkinter per creare una finestra GUI.

3. Definizione di funzioni per selezionare un video e una cartella: vengono definite due funzioni, `seleziona_video()` e `seleziona_cartella()`, che utilizzano la libreria filedialog di tkinter per consentire all'utente di selezionare un video e una cartella.

4. Selezione del video: viene chiamata la funzione `seleziona_video()` per selezionare un file video. Se il percorso del video è stato selezionato correttamente, viene creato un oggetto `VideoCapture` di OpenCV per aprire il video selezionato.

5. Ciclo per ottenere i frame del video: viene eseguito un ciclo while per catturare i frame del video utilizzando i metodi `grab()` e `retrieve()` di OpenCV. I frame vengono ridimensionati a una dimensione specifica (1920x1080) e aggiunti alla lista `frames`.

6. Visualizzazione del primo frame del video: viene mostrato il primo frame del video utilizzando la funzione `imshow()` di OpenCV.

7. Ciclo per controllare la visualizzazione dei frame: viene eseguito un ciclo while infinito per gestire l'interazione dell'utente con il video. Vengono utilizzate diverse condizioni per controllare l'input dell'utente e gestire il cambio di frame, la cattura degli screenshot e la navigazione all'interno del video.

8. Rilascio delle risorse: alla fine, viene rilasciato il video utilizzando il metodo `release()` di OpenCV.

In generale, il codice permette di selezionare un video, visualizzarlo e catturare gli screenshot dei frame desiderati in una cartella specificata dall'utente. L'utente può navigare avanti e indietro tra i frame, catturare gli screenshot premendo il tasto spazio, riprodurre il video in sequenza premendo il tasto Invio e interrompere l'esecuzione dell'applicazione premendo il tasto Esc.

## Pre-elaborazione dei dati
Prima di utilizzare i dati per addestrare il modello, è necessario effettuare alcune operazioni di pre-elaborazione. Questo può includere il ridimensionamento dei frame del video per uniformarli a una dimensione specifica, la normalizzazione dei valori dei pixel, l'estrazione di determinate caratteristiche visive rilevanti o la suddivisione dei dati in un set di addestramento e un set di test per valutare le prestazioni del modello.

## Roboflow: per la labellizzazione delle immagini
Questo progetto orientato all'allenamento di un modello di machine learning per il riconoscimento delle boe nel mare, durante processo di sviluppo del progetto ho richiesto il coinvolgimento Roboflow utilizzato per la labellizzazione delle immagini, cioè per annotare manualmente le boe nelle immagini del dataset.
<div style="display: flex; justify-content: center;"> 
  <img src="https://blog.roboflow.com/content/images/2021/08/256.png" alt="Descrizione" width="auto" height="128">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDZiQLh-OuLCZf6hWbr2_7tAd3xUSuiPilMcprntD4rt36SegKYbNHsWTcYOb8gQYIdPuaVDrZHHb0uxAg9ViwnhxumVQG-H36bqifh7QWh0epo5cWZZyPiRJU_FQU0YY9dYrb0oBuA5S2_dPJXBLyAQ0CkyfdotuLi72kwPkulzvkWT6CW8iJjlkEpw/s320/grafico%20bello.png" alt="Descrizione" width="auto" height="256">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK_FScMynDKDs7yQWjqfknJFPK6Z9golKlp6NtKvyC7qltw3E1ypbAJvngvPHU2WWD_Wnoap-qLxSDC3zpeCoO-aVY6SefeRCjBmwkbfsC80NpHShkl02-4WV3VR8yoHyu8SYBC17e4avI6Yic7kH7fopfD4T-TeN4sFPfShBPrla34YNc2-Wts8sXUA/s320/immagine_2023-06-16_135346177.png" alt="Descrizione" width="auto" height="256">
</div>

## Codice Colab utilizzato
```python
!git clone https://github.com/ultralytics/yolov5
import torch
torch.hub.download_url_to_file('https://app.roboflow.com/ds/6fDcQZtyLu?key=NmliLrqyk5', 'roboflow.zip')
!unzip -q roboflow.zip -d /content/buoys && rm roboflow.zip
torch.hub.download_url_to_file('https://ultralytics.com/assets/coco128.zip', 'tmp.zip')
!unzip -q tmp.zip -d /content/datasets && rm tmp.zip
!cp /content/buoys/train/images/* /content/datasets/coco128/images/train2017/
!cp /content/buoys/train/labels/* /content/datasets/coco128/labels/train2017/
import yaml
with open('/content/yolov5/data/coco128.yaml', 'r') as file:
    data = yaml.safe_load(file)
data['names'][0] = 'buoy'
with open('/content/yolov5/data/coco128.yaml', 'w') as file:
    yaml.dump(data, file)
%cd /content/yolov5
%pip install -qr requirements.txt
!python train.py --img 640 --batch 16 --epochs 60 --data /content/yolov5/data/coco128.yaml --weights yolov5s.pt --cache
!python detect.py --weights runs/train/exp/weights/last.pt --img 640 --conf 0.25 --source https://youtu.be/gPqqcKuKyaI
```

## Descrizione del codice
Il codice Colab inizia clonando il repository di YOLOv5. Successivamente, viene scaricato un file ZIP dal servizio Roboflow contenente le immagini annotate delle boe. Il file ZIP viene estratto nella cartella "/content/buoys". Vengono anche scaricati e estratti i file ZIP del dataset COCO nella cartella "/content/datasets". Le immagini e

 le etichette delle boe annotate vengono quindi copiate nelle rispettive cartelle del dataset COCO.

Successivamente, viene aperto il file di configurazione "coco128.yaml" utilizzato da YOLOv5 per definire il dataset. Il nome della classe nell'elenco delle classi viene modificato in "buoy", che rappresenta la classe delle boe. Infine, il file di configurazione viene salvato.

Dopo aver impostato l'ambiente, viene eseguito l'addestramento del modello utilizzando il comando "python train.py". Vengono specificate diverse opzioni, come la dimensione delle immagini di input, il numero di epoche e il percorso del file di configurazione del dataset.

Infine, viene eseguita la fase di rilevamento delle boe sul video specificato utilizzando il comando "python detect.py". Vengono utilizzati i pesi allenati durante la fase di addestramento per effettuare la rilevazione.

## Conclusioni
Questo progetto dimostra come utilizzare Visual Studio per creare un video player personalizzato con funzionalità di avanzamento, retrocessione, stop e riproduzione. Successivamente, viene mostrato come utilizzare Roboflow per annotare manualmente le boe nelle immagini del dataset e Colab per scrivere il codice utilizzando il framework YOLOv5 e il dataset COCO. Il modello di riconoscimento delle boe viene quindi addestrato e testato sul video specificato.

Si noti che questo è solo un esempio di implementazione e potrebbero essere necessarie ulteriori personalizzazioni e ottimizzazioni per adattare il progetto alle esigenze specifiche.
