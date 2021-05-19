class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):
            result = target - num

            if result in seen:
                return[seen[result], i]
            else:
                seen[num] = i

        return []

