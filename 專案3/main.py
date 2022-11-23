import datasource as ds


def main():
    print("這裡是main function")
    list_data = ds.get_forecase_data(ds.tw_county_names["高雄"])
    for item in list_data:
        print(item["main"]["temp"])


if __name__ == "__main__":
    print("這裡是程式的執行點")
    main()
