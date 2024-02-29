#User function Template for python3
class Solution:
    def sumBitDifferences(self, arr, n):
        res = 0

        # Traverse over all bits
        for i in range(32):

            # Count the number of elements with i'th bit set
            count = 0
            for j in range(n):
                if ((arr[j] & (1 << i)) != 0):
                    count += 1

            # Add "count * (n - count) * 2" to the result
            res += (count * (n - count) * 2)

        return res


