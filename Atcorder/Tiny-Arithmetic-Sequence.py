import sys
# https://atcoder.jp/contests/abc201/tasks/abc201_a
# これが等差数列になるかを判定する問題
# nums = 5 1 3

A1, A2, A3 = map(int, input().split())
ans = "No"
# (A1,A2,A3)
if A3-A2 == A2-A1:
    ans = "Yes"
# (A1,A3,A2)
if A2-A3 == A3-A1:
    ans = "Yes"
# (A2,A1,A3)
if A3-A1 == A1-A2:
    ans = "Yes"
print(ans)

