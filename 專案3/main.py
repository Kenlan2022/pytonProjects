import datasource as ds
from secret import api_key
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, cities_dict):
        super().__init__()
        tk.Label(self, text="各縣市4天天氣預測", font=(
            'Arial', 20)).pack(padx=30, pady=30)  # 標題不能改

        # 建立存放按鈕的容器
        # button_frame = tk.Frame(self).pack() 這樣會先pack，傳出none
        button_frame = tk.Frame()
        button_frame.pack(padx=50, pady=(0, 30))

        # 設定grid的row數量
        grid_row_num = 3
        for index, cities in enumerate(cities_dict.items()):
            cname, ename = cities  # 將key,value拆到兩個變數中
            btn = tk.Button(
                button_frame, text=f"{cname}\n{ename}", width=10, padx=20, pady=5)
            btn.grid(row=index % grid_row_num, column=index//grid_row_num)
            btn.bind("<Button>", self.button_click)  # 按下後將button資訊傳出

    # 實體的方法

    def button_click(self, event):
        btn_text = event.widget["text"]  # attribute 是 widget
        name_list = btn_text.split("\n")
        cname = name_list[0]
        ename = name_list[1]
        print(f"{cname}--{ename}")
        city_forcast = ds.get_forcast_data(ename, api_key)
        print(cname)
        print(city_forcast)
        if hasattr(self, 'displayFrame'):  # 如果屬性有displayframe時刪除displayframe防止重複疊加框架
            self.displayFrame.destroy()
        self.displayFrame = DisplayFrame(
            self, data=city_forcast, text=f"{cname}", borderwidth=2, relief=tk.GROOVE)
        self.displayFrame.pack(fill=tk.BOTH, padx=50, pady=(0, 30))


class DisplayFrame(ttk.LabelFrame):
    def __init__(self, parent, data=None, **kwargs):  # **kwargs打包變成dict
        super().__init__(parent, **kwargs)
        self.city_data = data
        leftFrame = tk.Frame(self, width=200, height=200, bg="#ff0000")
        leftFrame.pack(side=tk.LEFT)

        centerFrame = tk.Frame(self, width=200, height=200, bg="#00ff00")
        centerFrame.pack(side=tk.LEFT)

        rightFrame = tk.Frame(self, width=200, height=200, bg="#0000ff")
        rightFrame.pack(side=tk.LEFT)


def main():
    window = Window(ds.tw_county_names)
    window.title("各縣市4天天氣預測")
    window.mainloop()

    # try:
    #     list_data = ds.get_forecase_data(ds.tw_county_names["金門"], api_key)
    # except Exception as e:
    #     print(e)
    #     return

    # for item in list_data:
    #     print(item["main"]["temp"])


if __name__ == "__main__":
    main()
