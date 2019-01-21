from datetime import datetime, timedelta

def main():
    current_time = datetime.now()
    print("Now:\t\t", current_time)

    yesterday = current_time - timedelta(days=1)
    print('Yesterday:\t', yesterday)

    some_date = '01/01/17 12:10:03.234567'
    dt_obj = datetime.strptime(some_date, "%d/%m/%y %H:%M:%S.%f")
    print("Some date:\t", dt_obj)

if __name__ == '__main__':
    main()
