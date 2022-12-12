import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


discount = {1: "早鳥", 2: "校外教學", 3: "大學生", 4: "20人團體"}
stations = {1: "南港", 2: "台北", 3: "板橋", 4: "桃園", 5: "新竹", 6: "苗栗",
            7: "台中", 8: "彰化", 9: "雲林", 10: "嘉義", 11: "台南", 12: "左營"}


class Window(tk.Tk):
    def __init__(self, start_station, end_staion):
        super().__init__()
        tk.Label(self, text="高鐵班次查詢", font=(
            'Arial', 20)).pack(padx=30, pady=30)  # 標題不能改
        self.start_station = stations[1]

        # 建立存放按鈕的容器
        button_frame = tk.Frame(self)
        button_frame.pack(padx=50, pady=(0, 30))


class stationListBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.list = tk.Listbox(Window, width=15)
        for self.station in stations:
            self.list.insert(self.staion)


class checkBox(tk.Tk):
    def __init__(self, discount_type):
        super().__init__()
        self.checkbotton = tk.Checkbutton(Window, text=f"{discount_type}", variable=f"{discount}", onvalue=1, offvalue=0, command=display_input}).pack()

        def display_input():
            print(checkBox.get())







def main():
    pass


if __name__ == "__main__":
    main()
