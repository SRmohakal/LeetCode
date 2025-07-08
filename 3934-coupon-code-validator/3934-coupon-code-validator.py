import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        ans = []

        for c, b, active in zip(code, businessLine, isActive):
            if active and b in valid:
                if c and re.fullmatch(r'[A-Za-z0-9_]+', c):
                    ans.append((valid[b], c))
        
        ans.sort()
        return [c for _, c in ans]