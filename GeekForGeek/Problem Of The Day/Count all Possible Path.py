#User function Template for python3

class Solution:
    def isPossible(self, paths):
        for i in range(len(paths)):
            c = 0
            for j in range(len(paths)):
                if paths[i][j] == 1:
                    c += 1
            if c%2 != 0:
                return 0
        return 1
