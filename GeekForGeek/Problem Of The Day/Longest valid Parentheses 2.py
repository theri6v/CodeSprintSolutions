class Solution:
    def maxLength(self, s):
        res = 0
        st = []
        st.append(-1)
        
        for i in range(len(s)):
            c = s[i]
            
            if c == '(':
                st.append(i)
            else:
                if st:
                    st.pop()
                
                if st:
                    res = max(res, i - st[-1])
                else:
                    st.append(i)
        
        return res
