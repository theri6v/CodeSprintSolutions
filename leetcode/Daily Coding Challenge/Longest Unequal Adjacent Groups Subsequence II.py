class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        WIDTH = 5
        MASK = (1 << WIDTH) - 1
        n = len(words)
        f_map = {}
        from_ = [0] * n
        global_max_f = max_i = 0
        for i in range(n - 1, -1, -1):
            w, g = words[i], groups[i]

            hash_val = sum((ord(ch) & MASK) << (k * WIDTH) for k, ch in enumerate(w))

            f = 0
            for k in range(len(w)):
                h = hash_val | (MASK << (k * WIDTH))
                max_f, j = f_map.get(h, (0, 0))
                if max_f > f and groups[j] != g:
                    f = max_f
                    from_[i] = j

            f += 1
            if f > global_max_f:
                global_max_f, max_i = f, i

            for k in range(len(w)):
                h = hash_val | (MASK << (k * WIDTH))
                if h not in f_map or f > f_map[h][0]:
                    f_map[h] = (f, i)

        ans = [''] * global_max_f
        i = max_i
        for k in range(global_max_f):
            ans[k] = words[i]
            i = from_[i]
        return ans
