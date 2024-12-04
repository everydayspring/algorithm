all_students = set(range(1, 31))

submitted_students = set(int(input()) for _ in range(28))

missing_students = list(all_students - submitted_students)

missing_students.sort()

print(missing_students[0])
print(missing_students[1])