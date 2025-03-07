from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        helper = Counter(arr)
        lucky_numbers = [val for val, freq in helper.items() if val == freq]
        return max(lucky_numbers) if lucky_numbers else -1
