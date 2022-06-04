import collections

l = [list(map(int, input().split())) for l in range(3)]
x = []
y = []
for i in range(3):
    x.append(l[i][0])

for i in range(3):
    y.append(l[i][1])
    
xx = ([k for k, v in collections.Counter(x).items() if v == 1])
yy = ([k for k, v in collections.Counter(y).items() if v == 1])
print(*xx,*yy)