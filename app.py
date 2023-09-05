import datetime

def main():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Hello, World!")
    print("Current Timestamp:", formatted_time)

if __name__ == "__main__":
    main()