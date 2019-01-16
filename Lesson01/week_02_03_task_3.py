def ask_user():
    ask = ''
    while ask != 'Fine':
        ask = input('How are you?').capitalize()


def main():
    ask_user()


if __name__ == '__main__':
    main()