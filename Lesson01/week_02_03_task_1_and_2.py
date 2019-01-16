names = ['Vasya', 'Masha', 'Petya', 'Valera', 'Sasha', 'Dasha']


def find_person(name):
    flag = False
    for n in names:
        if n == name:
            print('{} is found'.format(name))
            flag = True
            break

    if not flag:
        print('{} is not found'.format(name))

def main():
    find_person('Sasha')

    print(names.pop(0))


if __name__ == '__main__':
    main()