import qrcode
import os
from PIL import Image

def genera_qr_url():
    link = input("Inserisci il link per generare il codice QR: ")
    img = qrcode.make(link)
    return img

def genera_qr_wifi():
    # Chiedi all'utente di inserire i dettagli della rete WiFi
    ssid = input("Inserisci il nome della rete WiFi (SSID): ")
    password = input("Inserisci la password della rete WiFi: ")

    # Configura i dati per la connessione WiFi
    wifi_data = f'WIFI:T:WPA;S:{ssid};P:{password};;'
    
    # Genera il codice QR per la connessione WiFi
    img = qrcode.make(wifi_data)
    return img, ssid

# Chiedi all'utente di selezionare l'opzione desiderata
scelta = input("Seleziona un'opzione (1 per URL / 2 per WIFI): ")

if scelta == '1':
    img = genera_qr_url()
    directory = './URL'
elif scelta == '2':
    img, ssid = genera_qr_wifi()
    directory = './WiFi'
else:
    print("Opzione non valida. Esce dal programma.")
    exit()

# Verifica se la directory esiste, altrimenti creala
if not os.path.exists(directory):
    os.makedirs(directory)

# Chiedi all'utente se vuole salvare l'immagine
salva_immagine = input("Vuoi salvare l'immagine del codice QR? (s/n): ").lower()

if salva_immagine == 's':
    # Se è un codice QR WiFi, salva l'immagine con il nome del SSID
    if scelta == '2':
        percorso_immagine = os.path.join(directory, f'{ssid}.png')
    else:
        # Altrimenti, chiedi all'utente di inserire un nome per l'immagine
        nome_file = input("Inserisci il nome per l'immagine del codice QR: ")
        percorso_immagine = os.path.join(directory, f'{nome_file}.png')

    # Salva l'immagine nella directory con il nome scelto dall'utente
    img.save(percorso_immagine)

    print(f"L'immagine è stata salvata in: {percorso_immagine}")
else:
    # Apri e visualizza l'immagine direttamente
    try:
        img.show()
    except Exception as e:
        print(f"Impossibile aprire l'immagine: {e}")
