students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)

gryffindors2 = {student: "Gryffindor" for student in students}
print(gryffindors2)

for i, student in enumerate(students):
    print(i + 1, student)
