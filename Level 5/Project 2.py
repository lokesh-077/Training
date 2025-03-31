#Student Grade Analyzer
students = []
for i in range(5):
    name = input("Enter name :")
    grade = float(input("Enter grade :"))
    students.append((name,grade))
def avg(students):
    total = sum(grade for i,grade in students)
    return  total/len(students)
def count_stu(students):
    return sum(1 for i,grade in students if grade > 60)
average = avg(students)
passing_count = count_stu(students)
print(f"Average : {average : }")
print(f"Passing : {passing_count}")

