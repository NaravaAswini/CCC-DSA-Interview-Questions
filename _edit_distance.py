class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j] represents the minimum number of operations
        # required to convert word1[0..i-1] into word2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # Base case:
        # If word2 is empty, delete all characters from word1
        for i in range(m + 1):
            dp[i][0] = i
        # If word1 is empty, insert all characters of word2
        for j in range(n + 1):
            dp[0][j] = j
        # Fill the DP table using optimal substructure
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current characters are equal, no operation needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # If characters are different, choose the best operation
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Delete
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j - 1]) # Replace
        # The answer is stored in dp[m][n]
        return dp[m][n]
