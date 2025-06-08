class Solution:
    def solve(self, first, second, t, s, ind):
        if ind >= len(s):
            return False

        if first == None:
            first = int(s[ind])
            return self.solve(first, second, t, s, ind + 1)

        if second == None:
            fc = first * 10 + int(s[ind])
            r1 = self.solve(fc, second, t, s, ind + 1)
            r2 = False
            if s[ind] != '0':
                second = int(s[ind])
                r2 = self.solve(first, second, t, s, ind + 1)
            return r1 or r2

        if t == None:
            sc = second * 10 + int(s[ind])
            r = self.solve(first, sc, t, s, ind + 1)
            if r:
                return True
            if s[ind] == '0':
                return False

        t = int(s[ind]) + (t * 10 if t != None else 0)
        if t > first + second:
            return False

        if t == first + second:
            if ind == len(s) - 1:
                return True
            else:
                first = second
                second = t
                t = None

        return self.solve(first, second, t, s, ind + 1)

    def isSumString(self, s):
        return self.solve(None, None, None, s, 0)
