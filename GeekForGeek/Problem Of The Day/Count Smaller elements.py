class Solution:

    def merge(self, left, right):
        i, j = 0, 0
        cnt = 0
        m, n = len(left), len(right)
        sorted_arr = []

        # merging the left and right arrays while counting the inversions
        while i < m and j < n:
            if left[i][1] > right[j][1]:
                cnt += 1
                sorted_arr.append(right[j])
                j += 1
            else:
                sorted_arr.append(left[i])
                self.ans[left[i][0]] += cnt
                i += 1

        # appending remaining elements from left array
        while i < m:
            sorted_arr.append(left[i])
            self.ans[left[i][0]] += cnt
            i += 1

        # appending remaining elements from right array
        while j < n:
            sorted_arr.append(right[j])
            cnt += 1
            j += 1

        return sorted_arr

    def split(self, nums):
        # base case: if list has only one element, return the list
        if len(nums) == 1:
            return nums

        # finding the mid index of the list
        mid = (len(nums)) // 2

        # recursively splitting the list into left and right halves
        left, right = self.split(nums[:mid]), self.split(nums[mid:])

        # merging the left and right halves
        return self.merge(left, right)

    def constructLowerArray(self, arr):
        n = len(arr)
        # initializing ans list with zeros of length n
        self.ans = [0 for _ in range(n)]

        nums = []
        # creating a list of tuples with index and value pairs
        for i, num in enumerate(arr):
            nums.append((i, num))

        # splitting and merging the list of tuples while counting inversions
        sorted_arr = self.split(nums)

        return self.ans
