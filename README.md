# Image Encryption WebApp

This is a Flask web application for encrypting and decrypting images using the `cryptography.fernet` library. The encryption key and image dimensions are saved to an Excel file for later use in the decryption process.

## Features

- Upload an image to encrypt.
- Download the encrypted image.
- Upload the encrypted image to decrypt.
- Download the decrypted image.

## Project Structure

image-encryption-webapp/
├── static/
│ ├── css/
│ │ └── style.css
│ ├── uploads/
│ │ └── (uploaded files)
├── templates/
│ ├── index.html
│ ├── encrypt.html
│ └── decrypt.html
├── app.py
├── encryption_key.xlsx
├── .gitignore
└── README.md


## How to Run

1. Install the dependencies:
   ```sh
   pip install -r requirements.txt

2. Run the Flask application:
   python app.py

3. Open your browser and navigate to 'http://127.0.0.1:5000/'.

# Dependencies
   
Flask
cryptography
pandas
openpyxl
matplotlib
opencv-python   
