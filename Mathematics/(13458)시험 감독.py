N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for student in students:
    student -= B
    answer += 1
    if student <= 0:
        continue
    elif student > 0:
        d, m = divmod(student, C)
        if m != 0:
            answer += (d + 1)
        else:
            answer += d

print(answer)