# アンドパッド

import numbers


# add two numbers
# ブルートフォースよくない解き方
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums) #4
        for i in range(length-1): #0,1,2,3
            for j in range(i+1, length):
                if (nums[i]+nums[j] == target):
                    return [i,j]

# ブルートフォースよくない解き方
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums) #4
        for i in range(length-1): #0,1,2,3
            for j in range(i+1, length):
                if (nums[i]+nums[j] == target):
                    return [i,j]