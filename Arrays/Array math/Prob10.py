'''You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.'''

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        temp_ones = 0
        ans_ones = 0
        temp_L = 0
        temp_R = 0
        L = 0
        R = 0
        for i in range(len(A)):
            temp_ones = temp_ones + (1 if A[i] == '0' else -1)
            temp_R = i
            if ans_ones < temp_ones:
                ans_ones = temp_ones
                R = temp_R
                L = temp_L
            if temp_ones < 0:
                temp_ones = 0
                temp_L = i + 1
                temp_R = i + 1
                
        if ans_ones > 0:
            return [L+1, R+1]
        else:
            return []