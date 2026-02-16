#User function Template for python3
class Solution:
    def canAttend(self,arr):
        # Your Code Here
        arr.sort(key=lambda x: x[0])

    # Check for overlapping meetings
        for i in range(1, len(arr)):
            if arr[i][0] < arr[i - 1][1]:
                return False
        return True

