class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        is_flipped = [0] * n
        flip_count = 0
        curr_flip = 0

        for i in range(n):
            if i >= k:
                curr_flip ^= is_flipped[i - k]
            if arr[i] ^ curr_flip == 0:
                if i + k > n:
                    return -1
                flip_count += 1
                curr_flip ^= 1
                is_flipped[i] = 1

        return flip_count
