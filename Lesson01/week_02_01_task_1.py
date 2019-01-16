def main():
    age = input('Enter your age: ')
    try:
        a = int (age)
        if 0 < a < 6:
            print('You should go to kindergarten')
        elif 6 <= a < 17:
            print('You should go to school')
        elif 17 <= a < 23:
            print('You should go to college')
        elif 23 <= a < 150:
            print('Go to work, bastard!')
        else:
            print ('You have entered invalid value.')
    except (ValueError):
        print('You have entered invalid value.')


if __name__ == '__main__':
    main()