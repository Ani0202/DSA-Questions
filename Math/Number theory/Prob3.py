def finding(A):
    n = len(A)
    mul = 1
    for i in range(1, n+1):
        mul *= i
    rank = 1
    i = 0
    while i < n:
        mul = mul/(n-i)

        cr = 0
        j = i+1
        while j <= n-1:
            if A[j] < A[i]:
                cr = cr + 1
            j = j + 1
        rank = rank + cr * mul
        i = i + 1

    return int(rank%1000003)
        
    
print(finding('acb'))
        