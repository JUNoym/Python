result = "No"
a, b, c = map(int, input().split())

if a**2 + b**2 < c**2:
    result = "Yes"
else:
    result = "No"

print(result)
