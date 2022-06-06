N = int(input())
A = list(map(int, input().split()))
# print((A))
numList = [True for i in range(2001)]
# print(numList)

for num in A:
    numList[num] = False

# print(numList)

for i,v in enumerate(numList):
    if v:
        print(i)
        break