N = int(input())
dict = {}
height = []
for i in range(N):
    name, h = map(str, input().split())
    h = int(h)
    dict[name] = h
    height.append(h)
result = (sorted(height)[-2])


def return_key(d, hei):
    for k, v in d.items():
        if hei == v:
            return k


print(return_key(dict, result))
