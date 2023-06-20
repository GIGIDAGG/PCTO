# Progetto per il riconoscimento delle boe nel mare utilizzando YOLOv5

## Introduzione
Questo progetto è orientato all'allenamento di un modello di machine learning per il riconoscimento delle boe nel mare. Il processo di sviluppo del progetto coinvolge l'utilizzo di VS code per la realizzazione di un video player personalizzato che consente di scorrere il video avanti, indietro, stop, play e salvare i frame interessati. Successivamente, viene utilizzato Roboflow per la labellizzazione delle immagini, mentre Colab viene utilizzato per scrivere il codice utilizzando il framework YOLOv5 e il dataset COCO aggiungendoci il nostro dataset.
<div style="display: flex; justify-content: center;"> 
  <img src="https://i.imgur.com/MaC4WEi.png" alt="Descrizione" width="auto" height="200">
</div>

## Strumenti utilizzati
- VS Code: utilizzato per creare un video player personalizzato con funzionalità di avanzamento, retrocessione, stop, riproduzione e salvataggio.
- Roboflow: utilizzato per la labellizzazione delle immagini, cioè per annotare manualmente le boe nelle immagini del dataset.
- Colab: utilizzato per scrivere il codice utilizzando il framework YOLOv5 e il dataset COCO.
- YOLOv5: framework di deep learning utilizzato per l'addestramento del modello di riconoscimento delle boe.
- Dataset COCO: dataset di immagini ampiamente utilizzato per l'addestramento di modelli di riconoscimento oggetti.

## Workflow: Fasi progetto
<div style="display: flex; justify-content: center;">
  <img src="https://i.imgur.com/ZeWqbIQ.png" alt="Descrizione" width="auto" height="900">
</div>

- Raccolta dati: Vengono raccolte immagini o video che contengono boe nel mare.
- Creazione del video player in Python: Utilizzando librerie Python come OpenCV o Pygame, viene creato un video player che consente di visualizzare i file video o immagini per la cattura dei frame di boe.
- Labellamento manuale delle immagini tramite Roboflow: Le immagini raccolte vengono caricate su Roboflow, e vengono manualmente assegnate le etichette corrispondenti alle boe presenti in ciascuna immagine.
- Allenamento del modello di machine learning: Viene utilizzato il framework YOLOv5. Durante l'allenamento, il modello impara a riconoscere le boe nel mare in base alle etichette fornite durante il labellamento.
- Rilevamento delle boe in un qualsiasi file multimediale: Rilevare le boe in qualsiasi file multimediale, come immagini o video. Il modello di machine learning utilizza i parametri appresi durante l'allenamento per identificare e localizzare le boe nell'input fornito, restituendo le coordinate dei bounding box che le circondano.

## Raccolta dati
Per addestrare il modello di riconoscimento delle boe, è necessario raccogliere un ampio set di dati contenente video che mostrano boe nel mare. È importante acquisire sequenze di diversi tipi di boe, in diverse condizioni di illuminazione e di sfondo, al fine di rendere il modello più robusto e generale. Il dataset può essere arricchito con l'aggiunta di etichette che indicano la presenza o l'assenza di boe in ciascun frame del video.

## Descrizione del codice del video player
Questo codice utilizza le librerie OpenCV e tkinter per creare un'applicazione che consente di selezionare un video, visualizzarlo e catturare i frame desiderati. Ecco una descrizione dettagliata del codice:

1. Importazione delle librerie: vengono importate le librerie OpenCV e tkinter.

2. Creazione di una finestra GUI: viene creato un oggetto Tkinter per creare una finestra GUI.

3. Definizione di funzioni per selezionare un video e una cartella: vengono definite due funzioni, `seleziona_video()` e `seleziona_cartella()`, che utilizzano la libreria filedialog di tkinter per consentire all'utente di selezionare un video e una cartella.

4. Selezione del video: viene chiamata la funzione `seleziona_video()` per selezionare un file video. Se il percorso del video è stato selezionato correttamente, viene creato un oggetto `VideoCapture` di OpenCV per aprire il video selezionato.

5. Ciclo per ottenere i frame del video: viene eseguito un ciclo while per catturare i frame del video utilizzando i metodi `grab()` e `retrieve()` di OpenCV. I frame vengono ridimensionati a una dimensione specifica (1920x1080) e aggiunti alla lista `frames`.

6. Visualizzazione del primo frame del video: viene mostrato il primo frame del video utilizzando la funzione `imshow()` di OpenCV.

7. Ciclo per controllare la visualizzazione dei frame: viene eseguito un ciclo while infinito per gestire l'interazione dell'utente con il video. Vengono utilizzate diverse condizioni per controllare l'input dell'utente e gestire il cambio di frame, la cattura degli screenshot e la navigazione all'interno del video.
      - ### AVANTI FRAME BY FRAME
        ```python
        #Scorrimento avanti frame per frame cliccando il tasto 'd'
        if key == 100:
            if j < len(frames)-1:
                j = j + 1
                cv2.imshow('video', frames[j])
        ```
        Consente di navigare all'interno del video scorrendo quest'ultimo in avanti, cambiando di frame in frame ad ogni click.
      - ### INDIETRO FRAME BY FRAME
        ```python
        #Scorrimento indietro frame per frame cliccando il tasto 'a'
        if key == 97:
            if j > 0: #Condizione di controllo per verificare che ci siano frame precedenti a quello corrente
                j = j - 1
                cv2.imshow('video', frames[j])
            else:
                continue
        ```
        Consente di navigare all'interno del video scorrendo quest'ultimo all'indietro, cambiando di frame in frame ad ogni click.
      - ### CATTURA SCREENSHOT
        ```python
        #Salvataggio frame cliccando il tasto [spazio]
        if key == 32:
            if i == 0: #Condizione di controllo per selezione il percorso file 
                frame_path = seleziona_cartella()
            if frame_path: #Condizione di controllo per verificare l'esistenza di un percorso file di salvataggio dei frame
                fourK = cv2.resize(frames[j], (3840, 2160)) #Ridimensionamento del frame alla qualità originale del video
                cv2.imwrite(frame_path+'/frame'+str(i+1)+'.png', fourK)
                i = i + 1
            else:
                print("Nessuna cartella selezionata.")
        ```
        Consente la cattura degli screenshot all'interno del video durante lo scorrimento di esso.
      - ### AVANTI VELOCE CONTINUATIVO
        ```python
        #tasto play cliccando [invio]
        if key == 13:
            key = 0 #azzeramento valore ascii salvato
            while True: #ciclo iterativo per andare avanti frame per frame
                if j < len(frames)-1:
                    key = cv2.waitKey(10)
                    j = j + 1
                    cv2.imshow('video', frames[j])
                    if key == 13: #condizione per la rottura del ciclo
                        break
                else:
                    break
        ```
        Consente di navigare all'interno del video scorrendo quest'ultimo velocemente in avanti, premendo il tasto una sola volta oppure ripremendolo per fermarlo.
      - ### INDIETRO VELOCE CONTINUATIVO
        ```python
        #tasto play back cliccando [dell]
        if key == 8:
            key = 0 #azzeramento valore ascii salvato
            while True: #ciclo iterativo per lo scorrimento frame per frame
                if j > 0:
                    key = cv2.waitKey(10)
                    j = j - 1
                    cv2.imshow('video', frames[j])
                    if key == 8: #condizione per la rottura del ciclo
                        break
        ```
        Consente di navigare all'interno del video scorrendo quest'ultimo velocemente all'indietro, premendo il tasto una sola volta oppure ripremendolo per fermarlo.
8. Rilascio delle risorse: alla fine, viene rilasciato il video utilizzando il metodo `release()` di OpenCV.

In generale, il codice permette di selezionare un video, visualizzarlo e catturare gli screenshot dei frame desiderati in una cartella specificata dall'utente. L'utente può navigare avanti e indietro tra i frame, catturare gli screenshot premendo il tasto spazio, riprodurre il video in sequenza premendo il tasto Invio e interrompere l'esecuzione dell'applicazione premendo il tasto Esc.

## Pre-elaborazione dei dati
Prima di utilizzare i dati per addestrare il modello, è necessario effettuare alcune operazioni di pre-elaborazione. Questo può includere il ridimensionamento dei frame del video per uniformarli a una dimensione specifica, la normalizzazione dei valori dei pixel, l'estrazione di determinate caratteristiche visive rilevanti o la suddivisione dei dati in un set di addestramento e un set di test per valutare le prestazioni del modello.

## Roboflow: per la labellizzazione delle immagini
Questo progetto orientato all'allenamento di un modello di machine learning per il riconoscimento delle boe nel mare, durante questo processo di sviluppo del progetto è richiesto il coinvolgimento Roboflow che viene utilizzato per la labellizzazione delle immagini, cioè per annotare manualmente le boe nelle immagini del dataset.
<div style="display: flex; justify-content: center;"> 
  <img src="https://blog.roboflow.com/content/images/2021/08/256.png" alt="Descrizione" width="auto" height="128">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDZiQLh-OuLCZf6hWbr2_7tAd3xUSuiPilMcprntD4rt36SegKYbNHsWTcYOb8gQYIdPuaVDrZHHb0uxAg9ViwnhxumVQG-H36bqifh7QWh0epo5cWZZyPiRJU_FQU0YY9dYrb0oBuA5S2_dPJXBLyAQ0CkyfdotuLi72kwPkulzvkWT6CW8iJjlkEpw/s320/grafico%20bello.png" alt="Descrizione" width="auto" height="200">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK_FScMynDKDs7yQWjqfknJFPK6Z9golKlp6NtKvyC7qltw3E1ypbAJvngvPHU2WWD_Wnoap-qLxSDC3zpeCoO-aVY6SefeRCjBmwkbfsC80NpHShkl02-4WV3VR8yoHyu8SYBC17e4avI6Yic7kH7fopfD4T-TeN4sFPfShBPrla34YNc2-Wts8sXUA/s320/immagine_2023-06-16_135346177.png" alt="Descrizione" width="auto" height="200">
</div>

### Risultati training Roboflow

|    mAP    | precision |  recall   |
| --------- | --------- | --------- |
|   75.3%   |   85.2%   |   69.0%   |

## Problema: Rilevamento errato di una boa  come una persona nel database YOLOv5 COCO - Ipotesi di possibile causa

**Descrizione del problema:**

Nel database utilizzato da YOLOv5, si è riscontrato un comportamento anomalo durante il rilevamento di un'immagine contenente una boa parzialmente sommersa. Secondo la nostra ipotesi, il modello potrebbe interpretare erroneamente la boa come la testa di una persona di cui si vede solo la parte superiore.

**Dettagli del problema:**

- **Sintomo**: Quando viene presentata un'immagine contenente una boa mezza sommersa, il modello rileva erroneamente questa configurazione come la testa di una persona.
- **Cause possibili**:
  1. La forma e la configurazione della boa sommersa possono assomigliare a quelle di una persona in piedi o a una testa.
  2. La somiglianza visiva tra la boa e una persona potrebbe confondere il modello di rilevamento degli oggetti.

**Effetti**:

Il rilevamento errato della boa come una persona può portare a risultati imprecisi o inadeguati nell'applicazione che utilizza il modello YOLOv5. Ciò potrebbe influire negativamente sul corretto conteggio degli oggetti o sulla classificazione degli stessi.

**Possibili soluzioni**:

1. Aggiungere al set di addestramento del modello esempi di immagini contenenti boe, in modo che il modello possa apprendere la differenza tra una persona e una boa.
2. Utilizzare tecniche di data augmentation per creare varianti delle immagini di boa sommerse e di persone, in modo che il modello possa apprendere a distinguere le due classi.
3. Esplorare altre architetture di reti neurali o modelli di rilevamento degli oggetti che potrebbero essere più adatti a distinguere una boa da una persona in questa situazione specifica.

**Potenziali sfide**:

La correzione di questo problema richiede un'analisi accurata delle immagini e delle caratteristiche che potrebbero confondere il modello di rilevamento. Inoltre, potrebbe essere necessario bilanciare il riconoscimento accurato di boe e persone in altre situazioni per evitare effetti indesiderati in altri contesti di utilizzo del modello.
<div style="display: flex; justify-content: center;"> 
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6adIyipHKIZjDkMUljHlJ7pUqSH_aqFiULEVts1fEUry03JTUMjNh_VtT9iiQpt78s7IkATPNJZEAToIBC5iDXUrNeS08ItmRfsEEDJ0lQ5wMOCrln5h7VAN8LutBpzXaoN-P1UJ-EUaSOReh4wffXCqgOt65ryoeMyF9XnQQ5kjCSeb3sh2jJPR_2Q/s320/Immagine%20WhatsApp%202023-06-16%20ore%2013.08.14.jpg" alt="Descrizione" width="auto" height="128">
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
## Risultato finale
### Video riconoscimento boe
[![Video riconoscimento boe](https://img.youtube.com/vi/BJnXyAlrrwE/0.jpg)](https://www.youtube.com/watch?v=BJnXyAlrrwE)

Cliccando su questa immagine si verrà direttamente reindirizzati alla pagina del video dimostrativo


## Conclusioni
Questo progetto dimostra come utilizzare Visual Studio per creare un video player personalizzato con funzionalità di avanzamento, retrocessione, stop e riproduzione. Successivamente, viene mostrato come utilizzare Roboflow per annotare manualmente le boe nelle immagini del dataset e Colab per scrivere il codice utilizzando il framework YOLOv5 e il dataset COCO. Il modello di riconoscimento delle boe viene quindi addestrato e testato sul video specificato.

Si noti che questo è solo un esempio di implementazione e potrebbero essere necessarie ulteriori personalizzazioni e ottimizzazioni per adattare il progetto alle esigenze specifiche.
 ## Suddivisione Lavoro


