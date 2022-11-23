
import tkinter as tk


# def CreateWindow():
#     window = tk.Tk()
#     window.title("這是我第一個視窗")
#     btn = tk.Button(window, text="請按我", padx=20,
#                     pady=20, font=("arial", 16))
#     btn.pack(padx=50, pady=30)
#     window.mainloop()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我第一個視窗")
        tk.Button(self, text="請按我", padx=20, pady=20,
                  font=("arial", 16), command=self.userClick).pack(padx=50, pady=30)

    def userClick(self):
        print("userClick")


def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()
