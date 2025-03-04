class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)

        for i in range(len(nums)-k+1):
            sub=nums[i:i+k]
            for num in set(sub):
                freq[num]+=1
        
        helper=[num for num,cnt in freq.items() if cnt==1]
        return max(helper) if helper else -1