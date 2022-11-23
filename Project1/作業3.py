import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

class ImageButton(tk.Button):
    def __init__(self,parents,**kwargs):
        super().__init__(parents,**kwargs)
        bgImg1 = Image.open("bluebutton.png")
        self.tkImage = ImageTk.PhotoImage(bgImg1)
        self.config(image=self.tkImage,borderwidth=0)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        bgImg = Image.open("abg.jpg")
        self.tkImg = ImageTk.PhotoImage(bgImg)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=self.tkImg)
        mainCanvas.pack(fill=tk.BOTH,expand=True)

        hel36 = tkFont.Font(family="Helvetica",size=40,weight="bold")
        tk.Label(mainCanvas,text="職能發展學院",font="hel36",background="#C9C8CD",foreground="#888888").place(x=380,y=200)

        buttonFrame = tk.Frame(mainCanvas, background="#ffffff")
        buttonFrame.place(x=100,y=50)

        btn1 = ImageButton(buttonFrame,command=self.btnClick)
        btn1.pack()

        btn2 = ImageButton(buttonFrame,command=self.btnClick)
        btn2.pack()

    def btnClick(self):
        print("按了")

def main():
    window = Window()
    window.title("練習作業")
    window.geometry("800x533")
    window.resizable(0,0)
    window.mainloop()

if __name__ == "__main__":
    main()
