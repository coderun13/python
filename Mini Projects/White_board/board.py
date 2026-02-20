import tkinter as tk
from tkinter.colorchooser import askcolor

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Digital Whiteboard")
        self.root.geometry("800x600")

        self.color = "black"
        self.brush_size = 3
        self.old_x = None
        self.old_y = None

        self.controls = tk.Frame(self.root, bg="lightgray", pady=5)
        self.controls.pack(side="top", fill="x")

        tk.Button(self.controls, text="Color", command=self.change_color).pack(side="left", padx=5)
        tk.Button(self.controls, text="Clear All", command=self.clear_canvas).pack(side="left", padx=5)
        
        self.size_slider = tk.Scale(self.controls, from_=1, to=20, orient="horizontal")
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side="left", padx=10)

        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint) # B1-Motion is Left-Click + Drag
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        self.brush_size = self.size_slider.get()
        if self.old_x and self.old_y:

            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.brush_size, fill=self.color,
                                    capstyle="round", smooth=True)
        
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def change_color(self):
        color_data = askcolor(color=self.color)
        if color_data[1]:
            self.color = color_data[1]

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    Whiteboard(root)
    root.mainloop()