from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq=Counter(nums)
        for key,val in freq.items():
            if val>n//2:
                return key
        return -1

         