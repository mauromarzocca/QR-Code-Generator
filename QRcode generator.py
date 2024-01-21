import qrcode
import os
from PIL import Image

# Chiedi all'utente di inserire il link
link = input("Inserisci il link per generare il codice QR: ")

# Genera il codice QR
img = qrcode.make(link)

# Chiedi all'utente se vuole salvare l'immagine
salva_immagine = input("Vuoi salvare l'immagine del codice QR? (s/n): ").lower()

if salva_immagine == 's':
    # Verifica se la directory MyQRCode esiste, altrimenti creala
    directory = './MyQRCode'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Chiedi all'utente di inserire un nome per l'immagine
    nome_file = input("Inserisci il nome per l'immagine del codice QR: ")
    
    # Salva l'immagine nella directory con il nome scelto dall'utente
    percorso_immagine = os.path.join(directory, f'{nome_file}.png')
    img.save(percorso_immagine)

    print(f"L'immagine è stata salvata in: {percorso_immagine}")
else:
    # Apri e visualizza l'immagine direttamente
    try:
        img.show()
    except Exception as e:
        print(f"Impossibile aprire l'immagine: {e}")
