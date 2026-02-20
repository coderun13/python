from tkinter import *
from tkinter import messagebox
import base64

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
       
        enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]

        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def handle_operation():
    msg = text_input.get()
    k = key_input.get()
    mode = mode_var.get()

    if not msg or not k:
        messagebox.showwarning("Input Error", "Please enter both a message and a key!")
        return

    if mode == 1: # Encrypt
        result_val.set(encode(k, msg))
    elif mode == 2: # Decrypt
        try:
            result_val.set(decode(k, msg))
        except:
            messagebox.showerror("Error", "Invalid key or corrupted message!")

def reset():
    text_input.set("")
    key_input.set("")
    result_val.set("")

#GUI Setup
root = Tk()
root.geometry("400x450")
root.title("Secret Message Tool")
root.configure(bg="#2c3e50")

text_input = StringVar()
key_input = StringVar()
mode_var = IntVar(value=1)
result_val = StringVar()

Label(root, text="SECRET MESSAGE TOOL", font="arial 15 bold", fg="white", bg="#2c3e50").pack(pady=10)

Label(root, text="Enter Message:", font="arial 12", fg="white", bg="#2c3e50").pack()
Entry(root, textvariable=text_input, width=40, font="arial 12").pack(pady=5)

Label(root, text="Enter Secret Key:", font="arial 12", fg="white", bg="#2c3e50").pack()
Entry(root, textvariable=key_input, show="*", width=40, font="arial 12").pack(pady=5)

Label(root, text="Choose Mode:", font="arial 12", fg="white", bg="#2c3e50").pack()
Radiobutton(root, text="Encrypt", variable=mode_var, value=1, bg="#2c3e50", fg="white", selectcolor="#2c3e50").pack()
Radiobutton(root, text="Decrypt", variable=mode_var, value=2, bg="#2c3e50", fg="white", selectcolor="#2c3e50").pack()

Button(root, text="EXECUTE", width=20, bg="#27ae60", fg="white", command=handle_operation).pack(pady=10)
Button(root, text="RESET", width=20, bg="#e74c3c", fg="white", command=reset).pack()

Label(root, text="Result:", font="arial 12 bold", fg="white", bg="#2c3e50").pack(pady=10)
Entry(root, textvariable=result_val, width=40, font="arial 12", state="readonly").pack()

root.mainloop()