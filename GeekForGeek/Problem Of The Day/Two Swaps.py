class Solution:
    def checkSorted(self, arr):
        
        swap = 0
        for index, value in enumerate(arr):
            if value != index+1:
                arr[index], arr[value-1] = arr[value-1], arr[index]
                swap += 1
                if swap > 2:
                    return False
        if swap == 0:
            return True
        for index, value in enumerate(arr):
            if value != index+1:
                return False
        return swap == 2
        
        return False
