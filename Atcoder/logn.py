# 計算量O(logn)
def func(n):
    if n <= 1:
        return
    else:
        print(n)
        func(n/2)


func(100)
