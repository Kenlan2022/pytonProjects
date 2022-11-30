import datasource as ds
from secret import api_key
import tkinter as tk


class Window(tk.Tk):
    def __init__(self, cities_dict):
        super().__init__()
        tk.Label(self, text="各縣市4天天氣預測", font=(
            'Arial', 20)).pack(padx=30, pady=30)  # 標題不能改

        # 建立存放按鈕的容器
        # button_frame = tk.Frame(self).pack() 這樣會先pack，傳出none
        button_frame = tk.Frame(
            self, background="#cccccc", width=200, height=300)
        button_frame.pack(padx=50, pady=(0, 30))

        # 設定grid的row數量
        grid_row_num = 3
        for index, cities in enumerate(cities_dict.items()):
            cname, ename = cities  # 將key,value拆到兩個變數中
            tk.Button(button_frame, text=f"{cname}\n{ename}", command=self.button_click, padx=20, pady=5).grid(
                row=index % grid_row_num, column=index//grid_row_num)

    def button_click(self):
        print("user click")


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
