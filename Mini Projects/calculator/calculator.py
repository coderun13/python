import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            # eval() evaluates the string as a math equation
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
            
    elif button_text == "C":
        entry.delete(0, tk.END)
        
    else:
        entry.insert(tk.END, button_text)

#main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")

#Display Screen
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

#Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

#Place Buttons using a grid
row_val = 1
col_val = 0

for button in buttons:

    action = lambda x=button: on_click(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()