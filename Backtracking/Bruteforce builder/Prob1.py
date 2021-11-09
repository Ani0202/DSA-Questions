'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
'''

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        phone = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        t = ''
        self.findLetters(A, phone, ans, t, 0)
        return ans
        
    def findLetters(self, A, phone, ans, t, ind):
        if ind == len(A):
            ans.append(t)
            return
        
        for i in range(len(phone[int(A[ind])])):
            t += phone[int(A[ind])][i]
            self.findLetters(A, phone, ans, t, ind + 1)
            t = t[:-1]
