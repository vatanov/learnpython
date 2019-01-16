scores = [{'school_class': '1b',
           'scores': [4,2,5]
           },
          {'school_class': '5a',
           'scores': [5,2,5,4]
           },
          {'school_class': '11v',
           'scores': [3,3,2]
           }]

def get_class_average(scores, class_name):
    for i in scores:
        if i['school_class'] == class_name:
            return sum(i['scores']) / i['scores'].__len__()


def get_school_average(scores):
    school_average = []
    for i in scores:
        school_average.append(sum(i['scores']) / i['scores'].__len__())

    return sum(school_average) / school_average.__len__()


def main():
    print('1-B average score is:', get_class_average(scores, '1b'))
    print('5-A average score is:', get_class_average(scores, '5a'))
    print('11-V average score is:', get_class_average(scores, '11v'))

    print('Whole school average score is:', get_school_average(scores))


if __name__ == '__main__':
    main()