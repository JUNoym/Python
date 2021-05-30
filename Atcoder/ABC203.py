import collections

A = list(map(int, input().split()))


def has_duplicates(seq):
    return len(seq) != len(set(seq))


is_dup = (has_duplicates(A))

if A[0] == A[1] == A[2]:
    print(A[2])
if is_dup:
    result = ([k for k, v in collections.Counter(A).items() if v == 1])
    for v in result:
        print(v)
else:
    print(0)
# [解答]
a, b, c = map(int, input().split())
if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)
else:
    print(0)
# --------------------------------------------------
N, K = map(int, input().split())
result = 0

for i in range(1, N+1):
    for k in range(1, K+1):
        result += i*100 + 10*0 + k*1
print(result)
