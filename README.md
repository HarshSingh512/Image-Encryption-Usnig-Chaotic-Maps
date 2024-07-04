# Image Encryption WebApp

This is a Flask web application for encrypting and decrypting images using the `cryptography.fernet` library. The encryption key and image dimensions are saved to an Excel file for later use in the decryption process.

## Features

- Upload an image to encrypt.
- Download the encrypted image.
- Upload the encrypted image to decrypt.
- Download the decrypted image.

## Project Structure


- **`static/`**: Contains static files for the web application.
  - **`css/`**: CSS stylesheets for styling web pages.
    - `style.css`: Custom styles for the application.
  - **`uploads/`**: Directory where uploaded images are stored temporarily.

- **`templates/`**: HTML templates rendered by Flask for different pages.
  - `index.html`: Homepage for uploading images.
  - `encrypt.html`: Page displaying the encrypted image after encryption.
  - `decrypt.html`: Page for uploading encrypted images and displaying decrypted results.

- **`app.py`**: Flask application script containing routes and logic for encryption and decryption.

- **`encryption_key.xlsx`**: Excel file storing encryption keys and image dimensions.

- **`.gitignore`**: Git ignore file to exclude unnecessary files from version control.


## How to Run

1. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   
2. Run the Flask application:
   python app.py

3. Open your browser and navigate to 'http://127.0.0.1:5000/'.

# Dependencies
   
- Flask
- Cryptography
- Pandas
- Openpyxl
- Matplotlib
- Opencv-python   
