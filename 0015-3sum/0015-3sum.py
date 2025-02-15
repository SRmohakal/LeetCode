from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            lf, rt = i + 1, len(nums) - 1
            while lf < rt:
                total = val + nums[lf] + nums[rt]
                if total > 0:
                    rt -= 1
                elif total < 0:
                    lf += 1
                else:
                    ans.append([val, nums[lf], nums[rt]])

                    # moving left pointer to skip duplicates
                    lf += 1
                    while lf < rt and nums[lf] == nums[lf - 1]:
                        lf += 1
        
        return ans
