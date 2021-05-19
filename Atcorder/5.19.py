import sys

# nums = [2, 3, 41, 4]
# target = 6


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


if __name__ == "__main__":
    args = sys.argv
    inst = Solution()
    print(inst.twoSum(args[1] args[2]))
