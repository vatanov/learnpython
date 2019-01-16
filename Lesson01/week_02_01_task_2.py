def compare_strings(first_string, second_string):
    if first_string == second_string:
        return 1
    else:
        if second_string == 'learn':
            return 3
        else:
            return 2


def main():
    print(compare_strings('qwe', 'learn'))


if __name__ == '__main__':
    main()
