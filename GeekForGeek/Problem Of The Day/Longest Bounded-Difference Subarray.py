class Solution:
    def longestSubarray(self, arr, x):
        max = 0
        min = 0
        i = j = 0
        lres = rres = 0
        while j < len(arr):
            # print(i,j)
            if abs(arr[j] - arr[max]) <= x:
                if abs(arr[j] - arr[min]) <= x:
                    if abs(arr[j]) > abs(arr[max]):
                        max = j
                    elif abs(arr[j]) < abs(arr[min]):
                        min = j
                    j += 1
                    # print("if")
                else:
                    if (rres - lres) < j-i:
                        lres = i
                        rres = j
                    i = min+1
                    min = i
                    if max < min:
                        max = min
                    j = i+1
            else:
                if (rres - lres) < j-i:
                    lres = i
                    rres = j
                i = max+1
                max = i
                if min < max:
                    min = max
                j = i+1
                # print("else")
        
        if (rres - lres) < j-i:
            lres = i
            rres = j
        return arr[lres:rres]
