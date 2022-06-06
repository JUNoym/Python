def main():
    def judge():
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        a_ok, b_ok = True, True  # 1個前でA, Bの要素を使うことができるか？
        for i in range(N - 1):
            a0, a1 = A[i], A[i + 1]  # 前のA、今のA
            b0, b1 = B[i], B[i + 1]  # 前のB、今のB
            na_ok, nb_ok = False, False  # A[i+1]、B[i+1]を末尾として使えるか？
            if a_ok:  # 前の末尾がA[i]にできる場合
                na_ok |= abs(a0 - a1) <= K  # 次の末尾をA[i+1]にできるか判定
                nb_ok |= abs(a0 - b1) <= K  # 次の末尾をB[i+1]にできるか判定
            if b_ok:  # 前の末尾がB[i]にできる場合
                na_ok |= abs(b0 - a1) <= K  # 次の末尾をA[i+1]にできるか判定
                nb_ok |= abs(b0 - b1) <= K  # 次の末尾をB[i+1]にできるか判定
            a_ok, b_ok = na_ok, nb_ok  # 1つ次の要素の判定に移るので、古いフラグは捨てて書き換えます
        return a_ok or b_ok

    print("Yes" if judge() else "No")


if __name__ == '__main__':
    main()