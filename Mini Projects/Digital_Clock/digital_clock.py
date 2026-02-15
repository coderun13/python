import tkinter as tk
from time import strftime

def update_time():
    # Get current time in 'Hour:Minute:Second AM/PM' format
    string = strftime('%H:%M:%S %p')
    label.config(text=string)

    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(
    root, 
    font=('calibri', 40, 'bold'),
    background='black',
    foreground='cyan'
)

label.pack(anchor='center')

update_time()

root.mainloop()