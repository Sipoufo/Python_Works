import pandas

with open("file1.txt") as f1:
    list1 = [int(number) for number in f1.readlines()]

with open("file2.txt") as f2:
    list2 = [int(number) for number in f2.readlines()]

result = [number for number in list1 if (number in list2)]

print(result)