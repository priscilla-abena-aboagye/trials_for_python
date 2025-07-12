grades = {
    "English": 55,
    "Science": 88
}
grades_2 = {
    "Maths": 44,
    "Social": 66
}
grades.update(grades_2)
print(grades)
print(grades["English"])

print(grades.get("English"))
grades.clear()
print(grades)
