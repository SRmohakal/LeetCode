from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_of_digits(num: int) -> int:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10 
            return digit_sum
        
        for i, val in enumerate(nums):
            if sum_of_digits(val) == i:
                return i
        return -1
