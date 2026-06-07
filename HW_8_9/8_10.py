import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])
lines = lines[1:]

students = [
(
int(lines[i + 2][:-1]),
lines[i + 2][-1],
lines[i],
lines[i + 1],
lines[i + 3],
lines[i + 2]
)
for i in range(0, 4 * n, 4)
]

students.sort(key=lambda student: (student[0], student[1], student[2]))

result = [
f"{student[5]} {student[2]} {student[3]} {student[4]}"
for student in students
]

print("\n".join(result))
