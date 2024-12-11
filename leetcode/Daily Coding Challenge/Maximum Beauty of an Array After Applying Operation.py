#Approach 1: Regular Window

class Solution:
  def maximumBeauty(self, nums: list[int], k: int) -> int:
    ans = 0

    nums.sort()

    l = 0
    for r in range(len(nums)):
      while nums[r] - nums[l] > 2 * k:
        l += 1
      ans = max(ans, r - l + 1)

    return ans

-----------------------------------------------------------------------------------------------------

#Approach 2: Lazy Window

class Solution {
 public:
  int maximumBeauty(vector<int>& nums, int k) {
    // l and r track the maximum window instead of the valid window.
    int l = 0;
    int r = 0;

    ranges::sort(nums);

    for (r = 0; r < nums.size(); ++r)
      if (nums[r] - nums[l] > 2 * k)
        ++l;

    return r - l;
  }
};
