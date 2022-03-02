import random
# number = [2, 4, 6, 8]
# new_number = [n + 1 for n in number]
# print(new_number)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_number = [n * 2 for n in range(1, 5 )]
# print(new_number)

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_score = {student: random.randint(1, 100) for student in names}
passed_students = {key: value for (key, value) in students_score.items() if (value >= 70)}

print(passed_students)