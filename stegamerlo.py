import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import base64
import os

class StegaMerloSec:
    def __init__(self, root):
        self.root = root
        self.root.title("StegaMerloSec")
        self.root.geometry("700x520")
        self.root.configure(bg="#2c3e50")  # Blu scuro

        self.image_path = None
        self.password = tk.StringVar()

        tk.Label(root, text="StegaMerloSec", font=("Consolas", 22, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

        tk.Button(root, text="Carica Immagine", command=self.load_image, bg="#3498db", fg="white", font=("Consolas", 12)).pack(pady=5)

        self.image_label = tk.Label(root, text="Nessuna immagine caricata", bg="#2c3e50", fg="white", font=("Consolas", 10))
        self.image_label.pack()

        tk.Label(root, text="Password:", bg="#2c3e50", fg="white", font=("Consolas", 10)).pack(pady=(10, 0))
        tk.Entry(root, textvariable=self.password, show="*", width=30, font=("Consolas", 10)).pack(pady=5)

        self.text_entry = tk.Text(root, height=6, width=65, bg="#fceeed", fg="black", font=("Consolas", 10))
        self.text_entry.pack(pady=10)

        tk.Button(root, text="🔐 Nascondi Testo", command=self.hide_text, bg="#e67e22", fg="white", font=("Consolas", 12)).pack(pady=5)
        tk.Button(root, text="🔓 Estrai Testo", command=self.reveal_text, bg="#2ecc71", fg="white", font=("Consolas", 12)).pack(pady=5)

        tk.Label(root, text="POWERED BY ROY MERLO", bg="#2c3e50", fg="#9f5a5a", font=("Consolas", 9, "italic")).pack(side="bottom", pady=6)

    def load_image(self):
        file = filedialog.askopenfilename(filetypes=[("Immagini", "*.png *.bmp *.jpg *.jpeg *.webp")])
        if file:
            self.image_path = file
            self.image_label.config(text=f"Immagine selezionata: {os.path.basename(file)}")

    def hide_text(self):
        if not self.image_path:
            messagebox.showwarning("Attenzione", "Carica prima un'immagine.")
            return

        testo = self.text_entry.get("1.0", tk.END).strip()
        if not testo:
            messagebox.showwarning("Attenzione", "Inserisci del testo da nascondere.")
            return

        pwd = self.password.get()
        if not pwd:
            messagebox.showwarning("Attenzione", "Inserisci una password.")
            return

        try:
            salt = b"stega_merlo"
            key = PBKDF2(pwd, salt, dkLen=32)  # AES-256
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(testo.encode())
            payload = base64.b64encode(cipher.nonce + tag + ciphertext).decode()

            output_img = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Immagini", "*.png")])
            if output_img:
                lsb.hide(self.image_path, payload).save(output_img)
                messagebox.showinfo("Successo", f"Testo nascosto in: {output_img}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def reveal_text(self):
        if not self.image_path:
            messagebox.showwarning("Attenzione", "Carica prima un'immagine.")
            return

        pwd = self.password.get()
        if not pwd:
            messagebox.showwarning("Attenzione", "Inserisci la password.")
            return

        try:
            hidden = lsb.reveal(self.image_path)
            if not hidden:
                raise ValueError("Nessun testo trovato.")

            data = base64.b64decode(hidden)
            nonce = data[:16]
            tag = data[16:32]
            ciphertext = data[32:]

            key = PBKDF2(pwd, b"stega_merlo", dkLen=32)
            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            testo = cipher.decrypt_and_verify(ciphertext, tag).decode()

            self.text_entry.delete("1.0", tk.END)
            self.text_entry.insert(tk.END, testo)

        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile decifrare il testo: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StegaMerloSec(root)
    root.mainloop()


