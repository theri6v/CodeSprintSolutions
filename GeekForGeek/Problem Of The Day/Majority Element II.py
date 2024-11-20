class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        b = set(arr)  # Get unique elements
        a = []  # Store elements that occur more than n/3 times

        for x in b:
            count = 0  # Reset count for each unique element
            for i in range(n):
                if x == arr[i]:
                    count += 1
            if count > n / 3:  # Check if the count exceeds n/3
                a.append(x)

        a.sort()  # Sort the result
        return a if a else []
