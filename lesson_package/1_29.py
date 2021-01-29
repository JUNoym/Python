# 重複する数字を除外する問題
import sys


def contains(array, val):
    for item in array:
        if item == val:
            return True
    return False


def unique(array):
    ret = []
    for item in array:
        if False == contains(ret, item):
            ret.append(item)
    return ret


argv = sys.argv[1:]
output = unique(argv)
print(output)
