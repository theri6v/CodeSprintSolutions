class Solution:
    def countSubs(self, s):
        # suffix automaton structures
        sa = []
        link = []
        length = []
        next_state = []

        # create initial state (state 0)
        sa.append({})
        link.append(-1)
        length.append(0)

        last = 0  # points to the state representing the whole string so far

        for ch in s:
            cur = len(sa)
            sa.append({})
            length.append(length[last] + 1)
            link.append(0)

            p = last
            while p != -1 and ch not in sa[p]:
                sa[p][ch] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = sa[p][ch]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(sa)
                    sa.append(sa[q].copy())
                    length.append(length[p] + 1)
                    link.append(link[q])

                    while p != -1 and sa[p].get(ch, -1) == q:
                        sa[p][ch] = clone
                        p = link[p]

                    link[q] = link[cur] = clone

            last = cur

        # count distinct substrings
        ans = 0
        for i in range(1, len(sa)):
            ans += length[i] - length[link[i]]

        return ans
