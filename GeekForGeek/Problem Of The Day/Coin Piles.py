class Solution:
    def minimumCoins(self, A, k):
        # Step 1: Sort the coin values
        A.sort()

        # Step 2: Prepare prefix sum array
        n = len(A)
        pre = [0]
        for x in A:
            pre.append(pre[-1] + x)

        # Step 3: Initialize result with the sum of all coins
        res = pre[-1]
        j = 0

        # Step 4: Try each coin as base value to compare others with
        for i in range(n):
            # Move j forward until A[j] > A[i] + k
            while j < n and A[j] <= A[i] + k:
                j += 1

            # Calculate cost to reduce all coins greater than A[i]+k
            if j < n:
                large = pre[-1] - pre[j] - (n - j) * (A[i] + k)
            else:
                large = 0

            # Total cost = sum of smaller/equal values + cost to reduce big ones
            res = min(res, pre[i] + large)

        return res
