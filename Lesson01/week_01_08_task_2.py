answers = {'hello': "Hi!", 'how are you': 'Fine', 'bye': 'See you'}

def get_answer(question):
    return answers.get(question.lower(), 'Question is not found.')


def main():
    flag = True

    while flag:
        question = input ('Enter question: ')
        if question.lower() != 'exit':
            print(get_answer(question))
        else:
            flag = False


if __name__ == '__main__':
    main()
