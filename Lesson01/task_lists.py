list1 = [2, 3, 4, 5, 6, 7]
list1.append('Python')
print(list1[0])
print(list1[-1])
print(list1[2:5])
print(list1.__len__())
print(len(list1))

for i in list1:
    if i == 6:
        print(list1.index(i))

list1.remove('Python')
print(list1)
