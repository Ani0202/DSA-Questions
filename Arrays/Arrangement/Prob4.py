'''Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, nums):
        ind = len(nums)-1
        
        while ind>0:
            if nums[ind] > nums[ind-1]:
                nums[ind:] = sorted(nums[ind:])
                for i in range(ind,len(nums)):
                    if nums[i]>nums[ind-1]:
                        nums[i], nums[ind - 1] = nums[ind - 1], nums[i]
                        break
                return nums
            
            ind -=1
        
        nums.sort() 
        return nums                