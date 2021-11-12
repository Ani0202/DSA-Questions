'''A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain an arrival date 
and a departure date. 
He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time 
O(N log N) .'''

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()
        n = len(arrive)
        m = len(depart)
        p = 0
        j = 0
        for k in range(n):
            while j < m:
                if depart[j] <= arrive[k]:
                    p -=1
                    j = j + 1
                else:
                    break
            p = p + 1
            if p > K:
                return False
        return True