numList = [True for i in range(0,10)]
s = input()

for i in range(9):
    numList[int(s[i])]=False

for i in range(10) :
	if(numList[i]):
		print(i)