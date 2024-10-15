#User function Template for python3

class Solution:
    def subArraySum(self, numbers, targetSum):
        prefixSumMap = {0: 1}
        currentSum = 0
        subarrayCount = 0

        for num in numbers:
            currentSum += num
            requiredPrefixSum = currentSum - targetSum

            if requiredPrefixSum in prefixSumMap:
                subarrayCount += prefixSumMap[requiredPrefixSum]

            prefixSumMap[currentSum] = prefixSumMap.get(currentSum, 0) + 1

        return subarrayCount
