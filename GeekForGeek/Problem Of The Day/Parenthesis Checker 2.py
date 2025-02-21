
class Solution:
    def isBalanced(self, s):

        stack = []

        #iterating over the string.
        for char in s:

            #if opening bracket is encountered, we push it into stack.
            if char in ['{', '[', '(']:
                stack.append(char)

            #if closing bracket is encountered, we compare it with top of stack.
            else:

                if len(stack) == 0:
                    return False

                #if top of stack has opening bracket of same type, we pop the
                #top element continue iterating else we return false.

                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                        continue
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                        continue
                if char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                        continue
                return False

        #if stack becomes empty, we return true else false.
        if len(stack):
            return False
        return True
        # code here
