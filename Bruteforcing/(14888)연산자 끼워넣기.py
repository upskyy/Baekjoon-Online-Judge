N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value = -1000000001
min_value = 1000000001
 

def calculate(idx, num, add, sub, mul, div):
    global max_value, min_value
    if idx == N:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return

    if add:
        calculate(idx + 1, num + numbers[idx], add - 1, sub, mul, div)
    if sub:
        calculate(idx + 1, num - numbers[idx], add, sub - 1, mul, div)
    if mul:
        calculate(idx + 1, num * numbers[idx], add, sub, mul - 1, div)
    if div:
        calculate(idx + 1, int(num / numbers[idx]), add, sub, mul, div - 1)


calculate(1, numbers[0], add, sub, mul, div)
print(max_value)
print(min_value)
