A, B = map(int, input().split())
kokeibun = (A + B)
if kokeibun >= 15 and B >= 8:
    print("1")
elif kokeibun >= 10 and B >= 3:
    print("2")
elif kokeibun >= 3:
    print("3")
else:
    print("4")
