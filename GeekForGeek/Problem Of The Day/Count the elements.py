#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        b.sort()
        
        result = []
        
        for i in query:
            left , right = 0 ,n-1
            while left<=right:
                mid = (left+right)//2
                if b[mid]<= a[i]:
                    left = mid + 1
                else:
                    right = mid-1
            
            result.append(left)
            
        return result 
        
