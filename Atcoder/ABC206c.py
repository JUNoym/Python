from collections import Counter
n = int(input())
A = list(map(int, input().split()))
A.sort()
total = n*(n-1)//2

cnt = Counter(A)
dup = [(n*(n-1))//2 for n in cnt.values()]

print(total-sum(dup))
