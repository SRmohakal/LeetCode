class Solution:
    def punishmentNumber(self, n: int) -> int:
        def valid(sq, target, indx=0, temp_sum=0):
            if indx == len(sq):
                return temp_sum == target

            num = 0
            for i in range(indx, len(sq)):
                num = num * 10 + int(sq[i])
                if temp_sum + num > target:
                    break 
                if valid(sq, target, i + 1, temp_sum + num):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            sq = str(i * i) 
            if valid(sq, i):
                total += int(sq)

        return total
