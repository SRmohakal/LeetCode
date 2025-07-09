class Solution:
    @staticmethod
    def to_base(num, base):
        if num == 0:
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while num > 0:
            ans = digits[num % base] + ans
            num //= base
        return ans

    def concatHex36(self, n: int) -> str:
        n2 = n * n
        n3 = n * n * n

        hex_part = hex(n2)[2:].upper()             
        base36_part = self.to_base(n3, 36)          

        return hex_part + base36_part
