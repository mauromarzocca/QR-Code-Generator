# QR Code Generator

A Python Script which can convert some resources into QRCode

## Index

- [QR Code Generator](#qr-code-generator)
  - [Index](#index)
  - [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [File Structure](#file-structure)

## Introduction

This QRCode Generator is a simple Python program developed by Mauro Marzocca. It allows users to generate QR codes for URLs and WiFi networks. The program utilizes the `qrcode` library for QR code generation and the `PIL` (Pillow) library for image processing.

## Dependencies

The following dependencies are required to run the QRCode Generator:

- `qrcode`: A Python library to generate QR codes.
- `PIL` (Pillow): A Python Imaging Library used for opening, manipulating, and saving various image file formats.

You can install these dependencies using the following command:

```bash
pip install qrcode pillow
```

## Usage

1. Run the program and follow the on-screen instructions.
2. Select an option (1 for URL, 2 for WiFi, 0 to exit).
3. For URL:
   - Enter the link for which you want to generate the QR code.
   - Choose whether to save the QR code image or not.
   - If saving, provide a name for the image or choose to use the default name.
4. For WiFi:
   - Enter the WiFi SSID and password.
   - Choose whether to save the QR code image or not.
   - If saving, provide a name for the image or choose to use the default name.

## File Structure

The generated QR codes for URLs are saved in the ./URL directory.
The generated QR codes for WiFi networks are saved in the ./WiFi directory.
Example

Below is an example of using the QRCode Generator:

```bash
python QRcode generator.py
```

Author

Mauro Marzocca: GitHub
License

This project is licensed under the MIT License - see the LICENSE file for details.
