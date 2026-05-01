class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        F = 0
        for i in range(n):
            F += i * nums[i]
        
        max_val = F
        for k in range(1, n):
            F = F + total - n * nums[n - k]
            max_val = max(max_val, F)
        
        return max_val
        
