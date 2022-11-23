import requests


def get_forcase_data(cityName, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&appid={api_key}"
    response = requests.get(url)
    if response.ok:
        print("下載成功")
        allData = response.json()
        city = allData['city']
        return city

    raise Exception("下載失敗")
