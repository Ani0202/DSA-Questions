'''Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[correct]:
                i += 1
            else:
                nums[i], nums[correct] = nums[correct], nums[i]
                
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1