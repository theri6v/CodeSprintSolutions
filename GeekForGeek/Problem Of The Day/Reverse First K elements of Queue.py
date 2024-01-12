#User function Template for python3
'''
Function Arguments :
        @param  : q ( given queue to be used), k(Integer )
        @return : list, just reverse the first k elements of queue and return new queue
'''

#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        # code here
        return q[:k][::-1]+q[k:]
