import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

class ImageButton(tk.Button):
    def __init__(self,parents,**kwargs):
        super().__init__(parents,**kwargs)
        bgImage1 = Image.open("btn1.png")
        self.tkImage1 = ImageTk.PhotoImage(bgImage1)
        self.config(image=self.tkImage1,borderwidth=0)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #------建立背景------#
        bgImg = Image.open("bg.jpg")
        self.tkImage = ImageTk.PhotoImage(bgImg)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=self.tkImage)
        mainCanvas.pack(fill=tk.BOTH,expand=True)
        #End---建立背景------#
        
        #------建立label------#
        hel36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
        tk.Label(mainCanvas,text="職能發展學院",font="hel36",background="#C9C8CD",foreground="#888888").place(x=370,y=50)
        #End---建立label------#

        #------建立ButtonFrame------#
        buttonFrame = tk.Frame(mainCanvas, background="#ffffff")
        buttonFrame.place(x=100,y=50)
        #End---建立ButtonFrame------#

        #------建立Button------#
        btn1 = ImageButton(buttonFrame,command=self.btnClick)
        btn1.pack()

        btn2 = ImageButton(buttonFrame,command=self.btnClick)
        btn2.pack()
        #End---建立Button------#

    def btnClick(self):
        print("userClick")

def main():
    window = Window()
    window.title("Frame框架")
    window.resizable(0,0)  # 可以使用滑鼠改變視窗的大小
    window.geometry("820x1080")  # 設定window的大小和位置
    window.mainloop()


if __name__ == "__main__":
    main()
