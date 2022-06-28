import sys
sys.setrecursionlimit(10**6)

def func(x):
    if memo[x] != -1:
        return memo[x]
    if x == 0:
        memo[0] = 0
    elif x == 1:
        memo[1] = 1
    else:
        memo[x] = func(x-2) + func(x-1)
    return memo[x]

N = int(input())
memo = [-1] * (N+1)

print(func(N))

