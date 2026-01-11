from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task
        freq = Counter(tasks)
        # Step 2: Find the maximum frequency
        maxFreq = max(freq.values())
        # Step 3: Count how many tasks have this maximum frequency
        maxCount = sum(1 for task in freq if freq[task] == maxFreq)
        # Step 4: Apply greedy scheduling formula
        min_intervals = (maxFreq - 1) * (n + 1) + maxCount
        # Step 5: Return the maximum between total tasks and calculated intervals
        return max(len(tasks), min_intervals)
