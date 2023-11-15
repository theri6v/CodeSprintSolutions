#User function Template for python3
class Solution:

    def findString(self, N, K):

        def __init__(self):

            self.a=None

        def dfs(n,k,string,ans):

            if n==0:

                ans.add(string)

                return ans

                    

            for i in range(k):

                ans=dfs(n-1,k,string+str(i),ans)

                

            return ans

        

        def find(ele,string):

            vis.add(ele)

            if len(vis)==(K**N):

                self.a=string

                return True

            

            for y in graph[ele]:

                if y not in vis and find(y,string+y[-1]):

                    return True

            vis.remove(ele)

                

            return False

                          

        ans=set()     

        ans=dfs(N,K,'',ans)  

        graph={}

        for i in ans:        

            for z in range(K):

                ele=i[1:]+str(z)

                if ele in ans and ele!=i:

                    if i in graph:

                        graph[i].append(ele)

                            

                    else:

                        graph[i]=[ele]

              

        vis=set()

        for i in ans:

            if find(i,i):

                return self.a

        return self.a
