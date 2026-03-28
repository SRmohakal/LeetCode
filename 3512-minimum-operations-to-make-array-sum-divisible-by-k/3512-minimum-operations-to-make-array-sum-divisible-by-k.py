class Solution(object):
    def minOperations(self, nums, k):
        # summ = 0
        # for i in range(len(nums)):
        #     summ += nums[i]
        
        # cnt = 0
        # while summ % k != 0:
        #     summ -= 1
        #     cnt += 1

        # return cnt   

        return sum(nums) % k     