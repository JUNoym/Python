n = int(input())
nums = [int(e) for e in input().split()]
# print(nums)
maxNum = max(nums)
minNum = min(nums)
sum = 0
for i in nums:
    sum += i
print(minNum, maxNum, sum)
