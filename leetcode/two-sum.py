class Solution:
    #farm
    def twoSum(self, nums, target):
        seen = {}
        #lol
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i