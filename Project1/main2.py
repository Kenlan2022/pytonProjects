import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont


class ImageButton(tk.Button):
    def __init__(self, parents, **kwargs):
        super().__init__(parents, **kwargs)
        bgImage1 = Image.open('btn1.png')
        self.tkImage1 = ImageTk.PhotoImage(bgImage1)
        self.config(image=self.tkImage1, borderwidth=0)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #------建立背景------#
        bgImage = Image.open('bg.jpg')
        self.tkImage = ImageTk.PhotoImage(bgImage)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(0, 0, anchor=tk.NW, image=self.tkImage)
        mainCanvas.pack(fill=tk.BOTH, expand=True)  # canvans裡面有東西時就沒有寬高，要再展開
        #End---建立背景------#

        #------建立label------#
        helv36 = tkFont.Font(family="Helvetica", size=36, weight="bold")
        tk.Label(mainCanvas, text="職能發展學院", font=helv36,
                 background="#C9C8CD", foreground="#888888").place(x=200, y=60)
        #End---建立label------#

        #---建立ButtonFrame---#
        buttonframe = tk.Frame(mainCanvas, width=100,
                               height=300, background="#ffffff")
        buttonframe.place(x=30, y=50)
        #End建立ButtonFrame---#

        #------建立Button------#
        btn1 = ImageButton(buttonframe, command=self.btn1Click)
        btn1.pack()

        btn2 = ImageButton(buttonframe, command=self.btn1Click)
        btn2.pack()

        #End---建立Button------#

    def btn1Click(self):
        print("userClick")


def main():
    window = Window()
    window.title("Frame框架")
    window.geometry("640x427+300+200")
    window.resizable(0, 0)  # 可以用滑鼠改變視窗的大小
    window.mainloop()


if __name__ == "__main__":
    main()
