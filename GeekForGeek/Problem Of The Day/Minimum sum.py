#User function Template for python3


class Solution:
    def minSum(self, arr):
        n=len(arr)
        arr.sort()
        temp=[]
        temp1=[]
        for i in range(n):
            if i%2==0:
                temp.append(str(arr[i]))
            else:
                temp1.append(str(arr[i]))
        temp=''.join(temp).lstrip('0')
        temp1=''.join(temp1).lstrip('0')
        
        i=len(temp)-1
        j=len(temp1)-1
        carry=0
        result=[]
        while i>=0 or j>=0 or carry>0:
            sum1=carry
            if i>=0:
                sum1+=int(temp[i])
                i-=1
            if j>=0:
                sum1+=int(temp1[j])
                j-=1
            result.append(str(sum1%10))
            carry=sum1//10
        return ''.join(result[::-1])
