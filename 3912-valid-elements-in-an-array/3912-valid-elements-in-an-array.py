class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        if n == 1:
            return nums
        
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], nums[i])
        
        suf_max = [0] * n
        suf_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], nums[i])
        
        result = []
        for i in range(n):
            if i == 0 or i == n-1:
                result.append(nums[i])
            else:
                if nums[i] > pre_max[i-1] or nums[i] > suf_max[i+1]:
                    result.append(nums[i])
        
        return result