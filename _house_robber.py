class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        # Edge case: only one house
        if n == 1:
            return nums[0]
        # dp[i] = maximum money that can be robbed till house i
        dp = [0] * n
        # Base cases
        dp[0] = nums[0]                 # Only one house
        dp[1] = max(nums[0], nums[1])   # Choose best of first two houses
        # Fill dp array using 1D DP
        for i in range(2, n):
            dp[i] = max(
                dp[i - 1],          # Skip current house
                dp[i - 2] + nums[i]) # Rob current house
        return dp[n - 1]
