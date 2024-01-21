import qrcode
import os
from PIL import Image

def genera_qr_url():
    link = input("Inserisci il link per generare il codice QR: ")
    img = qrcode.make(link)
    return img, link

def genera_qr_wifi():
    # Chiedi all'utente di inserire i dettagli della rete WiFi
    ssid = input("Inserisci il nome della rete WiFi (SSID): ")
    password = input("Inserisci la password della rete WiFi: ")

    # Configura i dati per la connessione WiFi
    wifi_data = f'WIFI:T:WPA;S:{ssid};P:{password};;'
    
    # Genera il codice QR per la connessione WiFi
    img = qrcode.make(wifi_data)
    return img, ssid

def verifica_e_nome_file(directory, nome_file):
    percorso_immagine = os.path.join(directory, f'{nome_file}.png')
    count = 2
    while os.path.exists(percorso_immagine):
        risposta = input(f"Il file {nome_file}.png esiste già. Vuoi cambiare il nome? (s/n): ").lower()
        if risposta == 's':
            nome_file = input("Inserisci il nuovo nome per l'immagine del codice QR: ")
            percorso_immagine = os.path.join(directory, f'{nome_file}.png')
        elif risposta == 'n':
            percorso_immagine = os.path.join(directory, f'{nome_file}({count}).png')
            count += 1
        else:
            print("Scelta non valida. Continua con il nome esistente.")
    return percorso_immagine

def apri_qr_code(img):
    apri_immagine = input("Vuoi aprire il QR Code appena generato? (s/n): ").lower()
    if apri_immagine == 's':
        try:
            img.show()
        except Exception as e:
            print(f"Impossibile aprire l'immagine: {e}")

# Intestazione
print("QRCode Generator\nUn programma di Mauro Marzocca\n")

while True:
    # Chiedi all'utente di selezionare l'opzione desiderata
    scelta = input("Seleziona un'opzione (1 per URL / 2 per WIFI / 0 per uscire): ")

    if scelta == '0':
        print("Uscita dal programma.")
        break
    elif scelta == '1':
        img, link = genera_qr_url()
        directory = './URL'
        # Chiedi all'utente come chiamare l'immagine per gli URL
        nome_file = input("Inserisci il nome per l'immagine del codice QR URL: ")
    elif scelta == '2':
        img, ssid = genera_qr_wifi()
        directory = './WiFi'
        nome_file = ssid
    else:
        print("Valore non valido. Devi selezionare 1 per URL, 2 per WIFI o 0 per uscire.")
        continue

    # Verifica se la directory esiste, altrimenti creala
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Chiedi all'utente se vuole salvare l'immagine
    salva_immagine = input("Vuoi salvare l'immagine del codice QR? (s/n): ").lower()

    if salva_immagine == 's':
        percorso_immagine = verifica_e_nome_file(directory, nome_file)

        # Salva l'immagine nella directory con il nome scelto dall'utente
        img.save(percorso_immagine)

        print(f"L'immagine è stata salvata in: {percorso_immagine}")
        apri_qr_code(img)
    else:
        apri_qr_code(img)
