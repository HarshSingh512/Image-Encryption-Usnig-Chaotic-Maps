import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cryptography.fernet import Fernet
from flask import Flask, request, render_template, send_file, redirect, url_for
import cv2

app = Flask(__name__)

class KeyGen:
    def __init__(self, arg1, arg2, height, width):
        self.param1 = arg1
        self.param2 = arg2
        self.param3 = np.random.randint(256, size=(height, width, 3), dtype=np.uint8)  # Generate a random key array with the same shape as the image

def save_key_to_excel(file_path, key, height, width):
    key_str = key.decode('utf-8')  # Decode the bytes key to string
    df = pd.DataFrame({'Key': [key_str], 'Height': [height], 'Width': [width]})
    df.to_excel(file_path, index=False)

def load_key_from_excel(file_path):
    df = pd.read_excel(file_path)
    key_str = df['Key'][0]
    height = df['Height'][0]
    width = df['Width'][0]
    return key_str.encode('utf-8'), height, width  # Encode the string back to bytes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        file_path = os.path.join('static', 'uploads', file.filename)
        file.save(file_path)
        
        # Load the image
        img = mpimg.imread(file_path)

        # Get the dimensions of the image
        height = img.shape[0]
        width = img.shape[1]

        # Initialize KeyGen object
        key_gen = KeyGen(0.01, 3.95, height, width)

        # Generate encryption key
        encryption_key = Fernet.generate_key()

        # Encrypt the image
        fernet = Fernet(encryption_key)
        img_bytes = img.tobytes()
        enimg_bytes = fernet.encrypt(img_bytes)

        # Save the encrypted image bytes to a file
        enimg_file_path = os.path.join('static', 'uploads', 'encrypted_' + file.filename)
        with open(enimg_file_path, 'wb') as f:
            f.write(enimg_bytes)

        # Save the encryption key and image dimensions to an Excel file
        save_key_to_excel('encryption_key.xlsx', encryption_key, height, width)

        return render_template('encrypt.html', original_image=file_path, encrypted_image=enimg_file_path)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        file_path = os.path.join('static', 'uploads', file.filename)
        file.save(file_path)

        # Load the encrypted image bytes from the file
        with open(file_path, 'rb') as f:
            enimg_bytes = f.read()

        # Load the encryption key and image dimensions from the Excel file
        encryption_key, height, width = load_key_from_excel('encryption_key.xlsx')

        # Decrypt the image
        fernet = Fernet(encryption_key)
        decimg_bytes = fernet.decrypt(enimg_bytes)
        
        # Debugging: Print image dimensions and size of image bytes
        print("Dimensions of decrypted image:", height, width)
        print("Size of image bytes:", len(decimg_bytes))

        # Reshape the image bytes to the expected dimensions
        try:
            decimg = np.frombuffer(decimg_bytes, dtype=np.uint8).reshape((height, width, 3))
        except ValueError:
            # Resize the image to match expected dimensions
            decimg = cv2.resize(decimg, (width, height))

        # Save the decrypted image
        decimg_file_path = os.path.join('static', 'uploads', 'decrypted_' + file.filename)
        mpimg.imsave(decimg_file_path, decimg)

        return render_template('decrypt.html', decrypted_image=decimg_file_path)

if __name__ == '__main__':
    app.run(debug=True)
