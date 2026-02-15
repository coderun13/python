
import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    """Function to create a new file by clearing the text area."""
    text_widget.delete(1.0, tk.END)

def open_file():
    """Function to open an existing text file."""
    filepath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if filepath:
        text_widget.delete(1.0, tk.END)
        
        try:
            with open(filepath, "r") as file:
                content = file.read()
                text_widget.insert(tk.END, content)
        except Exception as e:

            messagebox.showerror("Error", f"Failed to read file: {e}")

def save_file():
    """Function to save the content of the text area to a file."""
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filepath:
        text_content = text_widget.get(1.0, tk.END)
        
        try:
            with open(filepath, "w") as file:
                file.write(text_content)
    
            messagebox.showinfo("Success", "File saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

root = tk.Tk()
root.title("Simple Text Editor") 
root.geometry("800x600")  

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator() 
file_menu.add_command(label="Exit", command=root.quit)

text_widget = tk.Text(
    root,
    wrap=tk.WORD,          
    font=("Helvetica", 12),  
    fg="blue"             
)

text_widget.pack(expand=True, fill=tk.BOTH)

root.mainloop()