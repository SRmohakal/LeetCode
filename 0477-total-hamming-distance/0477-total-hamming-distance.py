class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)
        total=0

        for bit in range(32):
            count1=sum((num>>bit)&1 for num in nums)
            count0=n-count1
            total+=count1*count0
        
        return total