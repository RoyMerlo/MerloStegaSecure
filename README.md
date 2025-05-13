# 🕵️‍♂️ StegaMerloSec



**StegaMerloSec** is a graphical steganography tool that allows users to securely hide and extract encrypted text inside image files. It combines **AES-256 encryption** with **LSB steganography** for a double layer of data protection, all within a stylish and simple **Tkinter** GUI.

---
![20250513_2227_MerloStegaSecure 1 0_simple_compose_01jv5n77bzffvt04nnw6aps122](https://github.com/user-attachments/assets/6fe7b67f-1eb2-464a-b609-027042a69966)

## 🔐 Features

- 📷 Hide text messages inside PNG, BMP, JPG, JPEG, and WEBP images
- 🛡️ Encrypts hidden text using **AES-256** (EAX mode) for strong confidentiality
- 🔐 Password-protected text embedding and extraction
- 💾 Save new stego-images to desired location
- 🖥️ Intuitive and elegant GUI made with Tkinter
- 🧪 Displays error messages for incorrect decryption or missing inputs
- ⚡ "Powered by Roy Merlo" branding included

---

## 🛠 Requirements

Install required packages using pip:

```bash
pip install stegano pycryptodome


<img src="https://img.shields.io/badge/status-attivo-green" />
<img src="https://img.shields.io/badge/made%20with-Python-blue" />

🚀 How to Run
bash
Copy
Edit
python stegamerlo.py
🧰 How It Works
🔐 Hiding Text
Click "Carica Immagine" to load a cover image.

Enter the text to hide.

Enter a password.

Click "🔐 Nascondi Testo" and choose a location to save the new image.

The text is encrypted using AES-256 and embedded inside the image using LSB steganography.

🔓 Revealing Text
Load the image containing hidden text using "Carica Immagine".

Enter the same password used for hiding.

Click "🔓 Estrai Testo".

If the password is correct, the original text is decrypted and displayed.

📂 File Types Supported
Input image formats: .png, .bmp, .jpg, .jpeg, .webp

Output image format: .png (recommended for minimal compression)

⚠️ Security Notes
AES encryption uses a hardcoded salt (stega_merlo) for key derivation.

For production-grade applications, make salt dynamic and securely stored.

The system uses EAX mode for both confidentiality and integrity.

✨ Credits
GUI and logic by Roy Merlo

Steganography via stegano library

Cryptography via pycryptodome

📃 License
This project is open-source and free to use for educational or personal projects.


