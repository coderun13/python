import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file:
        root.title(f"{file} - Notepad")
        text_area.delete(1.0, tk.END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())

def save_file():
    file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))
        root.title(f"{file} - Notepad")

def quit_app():
    root.destroy()

# GUI
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

# Text Area
text_area = tk.Text(root, font=("Lucida Console", 12), undo=True)
text_area.pack(expand=True, fill="both")

# Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

root.mainloop()