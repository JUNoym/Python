import sys
sys.setrecursionlimit(10**6)
def func(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    return func(N-1) + func(N-2)

N = int(input())

print(func(N))