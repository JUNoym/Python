# 西暦N年が与えられ　そのN年が何世紀かを出力するプログラム。
import math

N = int(input())

print(math.floor((N+99)/100))
