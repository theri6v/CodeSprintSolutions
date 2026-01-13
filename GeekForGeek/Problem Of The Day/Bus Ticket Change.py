class Solution:
    def canServe(self, arr):
        # code here 
        
        if len(arr) == 0:
            return True
        
        change_5 = 0
        change_10 = 0
        
        for i in arr:
            if i == 5:
                change_5 = change_5 + 1
            elif i == 10:
                if change_5:
                    change_5 = change_5 - 1
                    change_10 = change_10 + 1
                else:
                    return False
            else:
                if not change_5:
                    return False
                else:
                    if change_10:
                        change_10 -= 1
                        change_5 -= 1
                    else:
                        if change_5 > 2:
                            change_5 -= 3
                        else:
                            return False
        
        return True
        
