import requests


api_key = "1b9553d7078c05ee58c7baa6a6930fe6"
cityName = "Taipei"


def get_forecase_data():
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&APPID={api_key}&lang=zh_tw&units=metric"

    response = requests.get(url=url)

    if response.ok:
        print("下載成功")
        return response.json()["list"]
    else:
        print("下載失敗")
