import tkinter as tk
from tkinter import messagebox
import random
import string

def create_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password should be at least 4 characters!")
            return
            
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(chars, length))
        
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        result_entry.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

# GUI Setup
root = tk.Tk()
root.title("Secure Pass")
root.geometry("350x250")
root.configure(bg="#2c3e50")

tk.Label(root, text="Password Length:", bg="#2c3e50", fg="white").pack(pady=10)
length_entry = tk.Entry(root, justify='center')
length_entry.pack()
length_entry.insert(0, "12")

tk.Button(root, text="Generate", command=create_password, bg="#27ae60", fg="white").pack(pady=20)

result_entry = tk.Entry(root, font=("Courier", 12), width=25, state="readonly", justify='center')
result_entry.pack()

root.mainloop()