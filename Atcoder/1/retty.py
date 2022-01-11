def solution(A):
    mother_collection = [i for i in range(1, 100001)]

    for num in A:
        if num > 0 and mother_collection[num - 1] == num:
            mother_collection.remove(num)

    result = min(mother_collection)
    return result

# これはデモタスクです。

# 関数を書いてください。

# def solution(A)

# N 個の整数の配列 A が与えられたとき、A の中に現れない最小の正の整数（0 より大きい）を返すもの。

# 例えば、A = [1, 3, 6, 4, 1, 2] が与えられたとき、この関数は 5 を返すべきである。

# A = [1, 2, 3] の場合、この関数は 4 を返すべきである。

# A = [-1, -3]のとき，この関数は1を返すべきである．

# 以下の仮定に対して，効率的なアルゴリズムを書け．

# Nは[1..100,000]の範囲にある整数である．
# 配列Aの各要素は，[-1,000,000...1,000,000]の範囲にある整数である．
