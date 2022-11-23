import tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        mainCanvas = tk.Canvas(self, width=640, height=427)
        self.tkImage = ImageTk.PhotoImage(Image.open("bg.jpg"))
        mainCanvas.create_image(0, 0, anchor=tk.NW, image=self.tkImage)
        tk.Button(mainCanvas, text="請按我").pack()
        mainCanvas.pack(fill=tk.BOTH, expand=True)  # canvans裡面有東西時就沒有寬高，要再展開


def main():
    window = Window()
    window.title("Frame框架")
    window.geometry("640x427")
    window.mainloop()


if __name__ == "__main__":
    main()
