# https://atcoder.jp/contests/arc121/tasks/arc121_a

from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from decimal import Decimal
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, combinations_with_replacement, product
from math import gcd, factorial, log2, ceil, floor, sin, asin, cos, acos, tan, atan, degrees
from pprint import pprint
from random import randrange
from sys import setrecursionlimit
from time import time
setrecursionlimit(10**9)
MOD = 10**9+7
INF = 10**18

# 考慮すべきは
# 同じものが複数あるパターン
#　→計算量が無限に多くなる恐れがある
#　　→値としてカウント出来れば良いので2つにまとめる
# 1位と2位が同じ組み合わせのx,y違いのパターン
#　→毎回chefを計算することによって、それを値として出さない

N = int(input())
X, Y = [], []
for n in range(N):
    _x, _y = map(int, input().split())
    X.append([_x, n])
    Y.append([_y, n])
x, y = copy(X), copy(Y)
x.sort()
y.sort()
# 上位2、下位2のインデックスの組み合わせをとる（重複排除）
idxes = set()
for i in [0, 1]:
    for j in [-1, -2]:
        _i, _j = min(x[i][1], x[j][1]), max(x[i][1], x[j][1])
        if (_i, _j) not in idxes:
            idxes.add((_i, _j))
for i in [0, 1]:
    for j in [-1, -2]:
        _i, _j = min(y[i][1], y[j][1]), max(y[i][1], y[j][1])
        if (_i, _j) not in idxes:
            idxes.add((_i, _j))


def chef(i, j):
    return max(abs(X[i][0]-X[j][0]), abs(Y[i][0]-Y[j][0]))


maxes = []
for i, j in idxes:
    maxes.append(chef(i, j))
maxes.sort(reverse=True)
print(maxes[1])
