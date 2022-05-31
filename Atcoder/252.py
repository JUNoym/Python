N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
like_food = max(A)
dislike_food_idx = []
flag = False
for i, f in enumerate(A):
    # print(i+1,f)
    if f == like_food:
        dislike_food_idx.append(i+1)

for j in B:
    if j in dislike_food_idx:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
