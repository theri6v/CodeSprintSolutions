#User function Template for python3

import re
class Solution:
    def match(self, wild, pattern):
        regex = re.escape(wild).replace(r"\*", ".*").replace(r"\?", ".")
        return re.fullmatch(regex, pattern) is not None
