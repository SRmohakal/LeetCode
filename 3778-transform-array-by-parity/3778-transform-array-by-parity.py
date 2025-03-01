class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = [0 if num % 2 == 0 else 1 for num in nums]
        ans.sort()
        return ans