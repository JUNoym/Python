import sys
sys.setrecursionlimit(10**6)

def func(N):
    if memo[N]!=-1:
        return memo[N]
    if N==0:
        memo[N] = 0
    elif N==1: 
        memo[N] = 1
    else:
        memo[N] = func(N-1) + func(N-2)
    return memo[N]

N = int(input())
memo = [-1] * (N+1)
print(func(N))