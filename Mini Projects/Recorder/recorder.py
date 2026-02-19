import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
from scipy.io.wavfile import write
import threading

def record_audio():
    try:
      
        seconds = int(duration_entry.get())
        fs = 44100  # Sample rate (standard CD quality)
        
    
        status_label.config(text="🔴 Recording...", fg="red")
        root.update()


        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished

        # Save the file
        write("output.wav", fs, recording)
        
        status_label.config(text=" Recording Saved!", fg="green")
        messagebox.showinfo("Success", "Audio saved as 'output.wav'")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of seconds")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_thread():
    thread = threading.Thread(target=record_audio)
    thread.start()

# GUI
root = tk.Tk()
root.title("Python Voice Recorder")
root.geometry("300x300")
root.configure(bg="#2c3e50")

tk.Label(root, text="Voice Recorder", font="arial 15 bold", bg="#2c3e50", fg="white").pack(pady=20)

tk.Label(root, text="Enter Duration (sec):", bg="#2c3e50", fg="white").pack()
duration_entry = tk.Entry(root, font="arial 12", justify='center')
duration_entry.pack(pady=5)
duration_entry.insert(0, "5")

status_label = tk.Label(root, text="Ready to Record", bg="#2c3e50", fg="white", font="arial 10 italic")
status_label.pack(pady=10)

btn = tk.Button(root, text="START RECORDING", font="arial 12 bold", bg="#e74c3c", fg="white", 
                command=start_thread, padx=10, pady=5)
btn.pack(pady=20)

root.mainloop()