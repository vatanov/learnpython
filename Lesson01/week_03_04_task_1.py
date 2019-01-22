from Lesson01.week_01_08_task_2 import answers
import csv

def main():
    print(answers)
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['how are you', 'bye', 'hello']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        writer.writerow(answers)


if __name__ == '__main__':
    main()
