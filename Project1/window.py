import tkinter as tk

win = tk.Tk()
win.title("標籤元件")
win.geometry("400x100")
lb101 = tk.Label(win, text="跟著實務學習ASP.NET Core MVC",
                 bg="pink", font=("標楷體", 16))
lb102 = tk.Label(win, text="跟著實務學習網頁設計", bg="yellow", font=("標楷體", 14))
lb103 = tk.Label(win, text="跟著實務學習Bootstrap", bg="red", font=("標楷體", 11))
lb101.pack()
lb102.pack()
lb103.pack()
win.mainloop()
