'''Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.'''

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        arr = sorted(map(str, nums), key=LargerNumKey)
        largest_num = "".join(arr)
        if largest_num[0] == '0':
            return '0'
        else: 
            return largest_num