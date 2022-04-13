# n x n の二次元配列を左向きに90°回転させるメソッドのテストを書け
def rotate(array):
    n = len(array)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            array[i][j], array[j][n - i - 1], array[n - i - 1][n - j - 1], array[n - j - 1][i] = array[n - j - 1][i], array[i][j], array[j][n - i - 1], array[n - i - 1][n - j - 1]
    return array