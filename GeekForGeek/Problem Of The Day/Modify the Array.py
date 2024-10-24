#User function Template for python3

class Solution:

    def modifyAndRearrangeArr(self, arr):
        #Complete the function
        n = len(arr)
        ans = []

        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                ans.append(2 * arr[i])
                arr[i + 1] = 0
            elif arr[i] == 0:
                ans.append(0)
            else:
                ans.append(arr[i])

        # Handle the last element
        if n > 1 and arr[n - 2] == arr[n - 1]:
            ans.append(0)
        elif n > 0:
            ans.append(arr[n - 1])

        # Create the modified list
        mod = []
        zero_count = 0

        for value in ans:
            if value != 0:
                mod.append(value)
            else:
                zero_count += 1

        # Append the counted zeros at the end
        mod.extend([0] * zero_count)

        return mod
