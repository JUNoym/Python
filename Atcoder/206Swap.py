from collections import Counter
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
_sorted = sorted(A)
# print(A) # [7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4]
print(_sorted)
total = N*(N-1) // 2
d = defaultdict(int)

for key in _sorted:  # [1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9, 9]
    total -= d[key]
    d[key] += 1
print(total)

# import random
# import string
# n = 1090
# _str = ''.join([random.choice(string.ascii_uppercase) for i in range(n)])
# print(_str)

# d = {}

# for key in _str:
#     if key not in d:
#         d[key] = 0
#     d[key] += 1
# print(d)
