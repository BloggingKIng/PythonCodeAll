
students = [
    {'name':'Alex', 'age': 12, 'isTall':True},
    {'name':'Ben', 'age': 10, 'isTall': False},
    {'name':'Ali','age': 15, 'isTall': True}
]


for student in students:
    for key,value in student.items():
        print(key, " : ", value)
