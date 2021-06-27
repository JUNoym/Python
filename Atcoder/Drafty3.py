S = list(input())
print(S)
S_num = len(S)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_plus(x):
    if x == '+':
        return True
    else:
        return False


for i, string in enumerate(S):
    jg = is_int(string)
    jg2 = is_plus(string)
    if jg:
        num = int(string)  # 4 1
        del S[i:num+i+1]
    elif jg2:
        S.remove(string)
        add_str = S[i]
        # print(add_str)
        S.insert(i, add_str)


print(*S, sep='')
