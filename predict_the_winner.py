from typing import List
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] represents the maximum score difference
        # the current player can achieve from nums[i..j]
        dp = [[0] * n for _ in range(n)]
        # Base case: only one element left
        for i in range(n):
            dp[i][i] = nums[i]
        # Build the DP table for subarrays of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Minimax decision:
                # Choose the option that maximizes current player's advantage
                choose_left = nums[i] - dp[i + 1][j]
                choose_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(choose_left, choose_right)
        # Player 1 wins if score difference is non-negative
        return dp[0][n - 1] >= 0
