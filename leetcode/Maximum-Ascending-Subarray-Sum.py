class Solution:
    def maxAscendingSum(self, nums):
        sum = nums[0]
        x = nums[0]
        i = 1
        l = len(nums)
        while i < l:
            if nums[i] > nums[i-1]:
                x += nums[i]
            else:
                x = nums[i]
            sum = max(x, sum)
            i += 1
        return sum


# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
