from collections import Counter

def main():
    with open('random_text.txt', 'r', encoding='utf-8') as file:
        word_count = 0
        for line in file:
            words = line.split()
            word_count += Counter(words).__len__()
        print(word_count)

if __name__ == '__main__':
    main()
