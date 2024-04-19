#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        st1 = set()
        res = []
        i, j = 0, 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if arr1[i] not in st1:
                    st1.add(arr1[i])
                    res.append(arr1[i])
                i += 1
            else:
                if arr2[j] not in st1:
                    st1.add(arr2[j])
                    res.append(arr2[j])
                j+=1
        
        if i < n:
            while i < n:
                if arr1[i] not in st1:
                    st1.add(arr1[i])
                    res.append(arr1[i])
                i+=1
        
        if j < m:
            while j < m:
                if arr2[j] not in st1:
                    st1.add(arr2[j])
                    res.append(arr2[j])
                j+=1
        
        return res
