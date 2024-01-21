import qrcode
import os
from PIL import Image

def generate_qr_url():
    link = input("Enter the link to generate the QR code: ")
    img = qrcode.make(link)
    return img, link

def generate_qr_wifi():
    # Ask the user to enter WiFi network details
    ssid = input("Enter the WiFi network name (SSID): ")
    password = input("Enter the WiFi network password: ")

    # Configure WiFi connection data
    wifi_data = f'WIFI:T:WPA;S:{ssid};P:{password};;'
    
    # Generate QR code for WiFi connection
    img = qrcode.make(wifi_data)
    return img, ssid

def open_qr_code(img):
    try:
        img.show()
    except Exception as e:
        print(f"Unable to open the image: {e}")

# Header
while True:
    # Ask the user to select the desired option
    print("\nQRCode Generator\nA program by Mauro Marzocca\n")
    choice = input("Select an option (1 for URL / 2 for WiFi / 0 to exit): ")

    if choice == '0':
        print("\nThank you for using my program!\n\t - Mauro Marzocca - \n")
        break
    elif choice == '1':
        # Ask the user if they want to save the QR code image
        while True:
            save_image = input("Do you want to save the QR code URL image? (y/n): ").lower()
            if save_image in ('y', 'n'):
                break
            else:
                print("Enter a valid response (y/n).")

        if save_image == 'y':
            img, link = generate_qr_url()
            # Ask the user how to name the image for URLs
            file_name = input("Enter the name for the QR code URL image: ")

            # Check if the directory exists, otherwise create it
            directory = './URL'
            if not os.path.exists(directory):
                os.makedirs(directory)

            image_path = os.path.join(directory, f'{file_name}.png')
            count = 2
            while os.path.exists(image_path):
                response = input(f"The file {file_name}.png already exists. Do you want to change the name? (y/n): ").lower()
                if response == 'y':
                    file_name = input("Enter the new name for the QR code image: ")
                    image_path = os.path.join(directory, f'{file_name}.png')
                elif response == 'n':
                    image_path = os.path.join(directory, f'{file_name}({count}).png')
                    count += 1
                else:
                    print("Invalid choice. Continue with the existing name.")

            # Save the image in the directory with the name chosen by the user
            img.save(image_path)

            print(f"The image has been saved to: {image_path}")
        else:
            img, link = generate_qr_url()
            open_qr_code(img)

    elif choice == '2':
        img, ssid = generate_qr_wifi()
        # Ask the user if they want to save the QR code image
        while True:
            save_image = input("Do you want to save the QR code WiFi image? (y/n): ").lower()
            if save_image in ('y', 'n'):
                break
            else:
                print("Enter a valid response (y/n).")

        if save_image == 'y':
            # Check if the directory exists, otherwise create it
            directory = './WiFi'
            if not os.path.exists(directory):
                os.makedirs(directory)

            image_path = os.path.join(directory, f'{ssid}.png')
            count = 2
            while os.path.exists(image_path):
                response = input(f"The file {ssid}.png already exists. Do you want to change the name? (y/n): ").lower()
                if response == 'y':
                    ssid = input("Enter the new name for the QR code image: ")
                    image_path = os.path.join(directory, f'{ssid}.png')
                elif response == 'n':
                    image_path = os.path.join(directory, f'{ssid}({count}).png')
                    count += 1
                else:
                    print("Invalid choice. Continue with the existing name.")

            # Save the image in the directory with the name chosen by the user
            img.save(image_path)

            print(f"The image has been saved to: {image_path}")
        else:
            open_qr_code(img)

    else:
        print("Invalid value. You must select 1 for URL, 2 for WiFi, or 0 to exit.")
        continue
