class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here\
        mid = n // 2


        for i in range(mid):
            arr.insert(i * 2 + 1, arr.pop(mid + i))

        return arr
