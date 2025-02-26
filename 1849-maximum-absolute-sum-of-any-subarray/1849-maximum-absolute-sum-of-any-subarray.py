class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        min_sum=0
        temp_max=0
        temp_min=0

        for num in nums:
            temp_max=max(num,temp_max+num)
            max_sum=max(max_sum,temp_max)

            temp_min=min(num,temp_min+num)
            min_sum=min(min_sum,temp_min)

        return max(abs(max_sum),abs(min_sum))