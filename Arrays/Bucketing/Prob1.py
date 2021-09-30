'''Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
Return 1 for true or 0 for false.

Example:

Given [0.6, 0.7, 0.8, 1.2, 0.4] ,

You should return 1

as

0.6+0.7+0.4=1.7

1<1.7<2

Hence, the output is 1.

O(n) solution is expected.

Note: You can assume the numbers in strings don’t overflow the primitive data type and there are no leading zeroes in numbers. Extra memory usage is allowed'''

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        A = [float(i) for i in A]
        lists = [[], [], []]
        for i in A:
            if i < 2.0/3:
                lists[0].append(i)
            elif i < 1:
                lists[1].append(i)
            else:
                lists[2].append(i)
        
        for i in range(3):
            mx1, mx2, mx3 = -10, -10, -10
            mi1, mi2, mi3 = 3, 3, 3
            for j in lists[i]:
                if j > mx1:
                    mx1, mx2, mx3 = j, mx1, mx2
                elif j > mx2:
                    mx2, mx3 = j, mx2
                elif j > mx3:
                    mx3 = j
            
                if j < mi1:
                    mi1, mi2, mi3 = j, mi1, mi2
                elif j< mi2:
                    mi2, mi3 = j, mi2
                elif j < mi3:
                    mi3 = j
            lists[i] = [mx1, mx2, mx3, mi1, mi2, mi3]
        
        
        a = lists[0]
        b = lists[1]
        c = lists[2]
        ls = []
        fc = a[0] + a[1] + a[2]
        ls.append(fc)
        fc = a[3] + a[4] + c[3]
        ls.append(fc)
        fc = a[3] + b[3] + b[4]
        ls.append(fc)
        fc = a[3] + b[3] + c[3]
        ls.append(fc)
        fc = b[0] + a[3] + a[4]
        ls.append(fc)
        if a[0] != a[3]:
            fc = b[0] + a[0] + a[3]
            ls.append(fc)
            fc = b[3] + a[0] + a[3]
            ls.append(fc)
        fc = b[3] + a[0] + a[1]
        ls.append(fc)
        for fc in ls:
            if fc > 1 and fc < 2:
                return 1
        return 0