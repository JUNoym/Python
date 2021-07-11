from collections import Counter
from collections import defaultdict

N, K = map(int, input().split())
p = list(map(int, input().split()))
print(p)
_sorted = sorted(p)
print(_sorted)

d = defaultdict(int)

while K > 0:
    if K >= N:
        for key in _sorted:
            d[key] += 1
            K -= 1
    else:
        d[0] += 1
        K -= 1

print(d)
