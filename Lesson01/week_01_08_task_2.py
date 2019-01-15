answers = {'hello': "Hi!", 'how are you': 'Fine', 'bye': 'See you'}

def get_answer(question):
    return answers.get(question.lower(), 'Question is not found.')


def main():
    while True:
        question = input ('Enter question: ')
        if question.lower() != 'exit':
            print(get_answer(question))
        else:
            break


if __name__ == '__main__':
    main()
