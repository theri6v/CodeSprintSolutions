#User function Template for python3

def max_sum(a,n):
    sums, sum_all = 0,0
    for i in range(n):
        sum_all += a[i]
        sums += a[i] * i
    maxm = sums    
    for i in range(1, n):
        sums = sums + sum_all - n * a[n - i]
        maxm = max(maxm, sums)
    return maxm
