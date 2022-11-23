import tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        mainCanvas = tk.Canvas(self, width=820, height=1080)
        btnimg = Image.open("fb.jpg").resize((150, 100), Image.ANTIALIAS)
        self.tkbtnimg = ImageTk.PhotoImage(btnimg)
        btn = tk.Button(mainCanvas, text="click",
                        imgage=self.tkbtnimg, compund=tk.LEFT).pack


def main():
    window = Window()
    window.title("Frame框架")
    window.resizable(0, 0)  # 可以使用滑鼠改變視窗的大小
    window.geometry("820x1080")  # 設定window的大小和位置
    window.mainloop()


if __name__ == "__main__":
    main()
