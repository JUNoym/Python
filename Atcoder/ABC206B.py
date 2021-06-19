n = int(input())
count = 0
result = 0

for i in range(1, 100000001):
    result += i
    count += 1
    if result >= n:
        break
print(count)
