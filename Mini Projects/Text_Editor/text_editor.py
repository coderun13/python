
import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    """Function to create a new file by clearing the text area."""
    # Delete all content from the beginning (1.0) to the end (tk.END)
    text_widget.delete(1.0, tk.END)

def open_file():
    """Function to open an existing text file."""
    # Use a file dialog to ask the user for a file path to open
    filepath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    # Check if a file was selected (i.e., the path is not empty)
    if filepath:
        # Clear the current content before inserting the new file's content
        text_widget.delete(1.0, tk.END)
        
        try:
            # Open the file in read mode ('r')
            with open(filepath, "r") as file:
                # Read the entire content of the file
                content = file.read()
                # Insert the content into the text widget at the beginning (tk.INSERT)
                text_widget.insert(tk.END, content)
        except Exception as e:
            # Display an error message if something goes wrong
            messagebox.showerror("Error", f"Failed to read file: {e}")

def save_file():
    """Function to save the content of the text area to a file."""
    # Use a file dialog to ask the user for a file path and name to save as
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    # Check if a file path was provided (i.e., the path is not empty)
    if filepath:
        # Get the current content from the text widget, from 1.0 to tk.END
        text_content = text_widget.get(1.0, tk.END)
        
        try:
            # Open the file in write mode ('w'). This will create the file or overwrite it.
            with open(filepath, "w") as file:
                # Write the text content to the file
                file.write(text_content)
            
            # Display a confirmation message
            messagebox.showinfo("Success", "File saved successfully!")
            
        except Exception as e:
            # Display an error message if saving fails
            messagebox.showerror("Error", f"Failed to save file: {e}")

root = tk.Tk()
root.title("Simple Text Editor") # Set the window title
root.geometry("800x600")       # Set the initial size of the window

menu_bar = tk.Menu(root)
root.config(menu=menu_bar) # Configure the root window to use this menu bar

file_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator() # Add a separator line
file_menu.add_command(label="Exit", command=root.quit) # Use root.quit to close the app

text_widget = tk.Text(
    root,
    wrap=tk.WORD,            # Wrap text at word boundaries
    font=("Helvetica", 12),  # Set the font style and size
    fg="blue"                # Set the foreground (text) color to blue
)

text_widget.pack(expand=True, fill=tk.BOTH)

root.mainloop()