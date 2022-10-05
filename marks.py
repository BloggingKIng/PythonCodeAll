student_marks = {'English':75, 'Maths':89, 'Biology':68}

i = 0

for marks in student_marks.values():
    i += marks
    print(i)


average_marks = i /len(student_marks)

print("Average Marks of student is {}".format(average_marks))
