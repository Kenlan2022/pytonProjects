import datasource


def main():
    print("這裡是main function")
    allData = datasource.get_forecase_data()
    print(allData)

if __name__ == "__main__":
    print("這裡是程式的執行點")
    main()
