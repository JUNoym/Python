A, B = map(int, input().split())
maxsum = 6*A
minsum = A
if minsum <= B <= maxsum:
    print('Yes')
else:
    print('No')
