from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_nums=set()

        for perm in permutations(digits,3):
            num=perm[0]*100 + perm[1]*10 + perm[2]

            if perm[0]!=0 and perm[2]%2==0:
                unique_nums.add(num)
        
        return len(unique_nums)