# A, B, C, D = map(int, input().split())

# count = 0
# tmp = 100000000
# red = 0
# ab = 0
# flag = True


# while tmp > D:
#     if B > C:
#         flag = False
#         break

#     count += 1
#     A += B
#     red += C
#     tmp = 0
#     tmp = A/red


# if flag:
#     print(count)
# else:
#     print(-1)


# 解答例
a, b, c, d = map(int, input().split())

ans = -1
for i in range(10**6):
    if a + (i * b) <= (i * c) * d:
        ans = i
        break

print(ans)
