A, B, C, D = map(int, input().split())

takahasiTime = A*60+B
aokiTime = C*60+D+1


if takahasiTime < aokiTime:
    print("Takahashi")
else:
    print("Aoki")