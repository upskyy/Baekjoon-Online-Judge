A = int(input())
B = input()
B = B[::-1]

for i in range(len(B)):
    print(A * int(B[i]))

B = B[::-1]

print(A * int(B))
