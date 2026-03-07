import tkinter as tk
from tkcalendar import Calendar

def get_selected_date():
    # Retrieve the date from the calendar widget
    date = cal.get_date()
    date_label.config(text=f"Selected Date: {date}")

# 1. Setup the main window
root = tk.Tk()
root.title("Python GUI Calendar")
root.geometry("400x450")
root.configure(bg="#34495e")

# 2. Add the Calendar Widget
# You can customize colors like headers, background, etc.
cal = Calendar(root, selectmode='day', 
               year=2024, month=5, day=23,
               background="#2c3e50", foreground="white", 
               headersbackground="#1abc9c", bordercolor="#1abc9c")

cal.pack(pady=20, padx=10, fill="both", expand=True)

# 3. Add a Button to capture the date
btn = tk.Button(root, text="Get Date", command=get_selected_date, 
                bg="#1abc9c", fg="white", font=("Arial", 12, "bold"))
btn.pack(pady=10)

# 4. Label to display the result
date_label = tk.Label(root, text="Select a date and click 'Get Date'", 
                      bg="#34495e", fg="white", font=("Arial", 12))
date_label.pack(pady=20)

root.mainloop()