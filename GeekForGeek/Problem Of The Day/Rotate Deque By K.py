class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        dq.rotate(k) if type==1 else dq.rotate(-k)
                
