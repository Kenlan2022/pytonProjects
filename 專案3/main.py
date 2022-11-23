import datasource


def main():
    print("這裡是main function")
    list_data = datasource.get_forecase_data()
    for item in list_data:
        print(item["main"]["temp"])


if __name__ == "__main__":
    print("這裡是程式的執行點")
    main()
