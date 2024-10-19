#User function Template for python3

class Solution:
    def roundToNearest (self, s) : 
        #Complete the function
        sys.set_int_max_str_digits(70000)
        x=int(s)
        temp=x//10
        rem=x%10
        lead_zero=len(s)-len(str(x))
        
        if rem>5:
            result = (temp * 10) + 10
        else:
            result = temp * 10
            
        ans='0'*lead_zero+str(result)
        return ans
