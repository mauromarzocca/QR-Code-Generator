# Generatore di Codici QR

Uno script Python in grado di convertire risorse in codici QR

## Indice

- [Generatore di Codici QR](#generatore-di-codici-qr)
  - [Indice](#indice)
  - [Introduzione](#introduzione)
  - [Dipendenze](#dipendenze)
  - [Utilizzo](#utilizzo)
  - [Struttura del File](#struttura-del-file)
  - [Esempio](#esempio)
  - [Autore](#autore)
  - [Licenza](#licenza)

## Introduzione

Questo Generatore di Codici QR è un semplice programma Python sviluppato da Mauro Marzocca. Consente agli utenti di generare codici QR per URL e reti WiFi. Il programma utilizza la libreria `qrcode` per la generazione di codici QR e la libreria `PIL` (Pillow) per l'elaborazione delle immagini.

## Dipendenze

Le seguenti dipendenze sono necessarie per eseguire il Generatore di Codici QR:

- `qrcode`: Una libreria Python per generare codici QR.
- `PIL` (Pillow): Una libreria di immagini Python utilizzata per l'apertura, la manipolazione e il salvataggio di vari formati di file immagine.

È possibile installare queste dipendenze utilizzando il seguente comando:

```bash
pip install qrcode pillow
```

## Utilizzo

1. Esegui il programma e segui le istruzioni visualizzate.
2. Seleziona un'opzione (1 per URL, 2 per WiFi, 0 per uscire).
3. Per URL:
   - Inserisci il link per il quale desideri generare il codice QR.
   - Scegli se salvare l'immagine del codice QR o meno.
   - Se si salva, fornisci un nome per l'immagine o scegli di utilizzare il nome predefinito.
4. Per WiFi:
   - Inserisci il nome SSID e la password del WiFi.
   - Scegli se salvare l'immagine del codice QR o meno.
   - Se si salva, fornisci un nome per l'immagine o scegli di utilizzare il nome predefinito.

## Struttura del File

- I codici QR generati per gli URL vengono salvati nella directory `./URL`.
- I codici QR generati per le reti WiFi vengono salvati nella directory `./WiFi`.

## Esempio

Di seguito è riportato un esempio di utilizzo del Generatore di Codici QR:

```bash
python QRcode generator_IT.py
```

## Autore

- **Mauro Marzocca**: [GitHub](https://github.com/mauromarzocca)

## Licenza

Questo progetto è distribuito con la Licenza MIT - consultare il file [LICENSE](LICENSE) per ulteriori dettagli.
