from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_sum = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1  

        for num in nums:
            prefix_sum += num
            cnt += prefix_cnt[prefix_sum - k]
            prefix_cnt[prefix_sum] += 1
        
        return cnt