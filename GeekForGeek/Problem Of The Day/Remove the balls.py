class Solution:
    def findLength(self, color, radius):
        stack = []

        for i in range(len(color)):
            flag = False
            while stack:
                top = stack[-1]
                if top[0] == color[i] and top[1] == radius[i]:
                    stack.pop()
                    flag = True
                else:
                    break
            if flag:
                continue
            else:
                stack.append((color[i], radius[i]))
        
        return len(stack)
