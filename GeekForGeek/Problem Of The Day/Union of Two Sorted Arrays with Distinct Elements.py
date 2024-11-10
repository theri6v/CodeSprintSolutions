#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        n1,n2=len(a),len(b)
        i,j=0,0
        ans=[]
        while i<n1 and j<n2:
            if a[i]==b[j]:
                ans.append(a[i])
                i+=1
                j+=1
            elif a[i]>b[j]:
                ans.append(b[j])
                j+=1
            else:
                ans.append(a[i])
                i+=1
        while i<n1:
            ans.append(a[i])
            i+=1
        while j<n2:
            ans.append(b[j])
            j+=1
            
        return ans
