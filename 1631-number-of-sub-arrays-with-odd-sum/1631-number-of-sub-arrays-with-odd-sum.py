class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD=10**9+7
        odd_cnt=0
        even_cnt=1
        prefix_sum=0
        ans=0

        for val in arr:
            prefix_sum+=val
            if prefix_sum%2==0:
                ans+=odd_cnt
                even_cnt+=1
            else:
                ans+=even_cnt
                odd_cnt+=1
            ans%=MOD
        
        return ans