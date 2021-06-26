N, A, B = map(int, input().split())
result = 0


def findNum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


for i in range(1, N+1):
    sum = findNum(i)
    if A <= sum <= B:
        result += i
print(result)
