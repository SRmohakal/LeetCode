class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_digit = {'0', '1', '2', '5', '6', '8', '9'}
        changing_digit = {'2', '5', '6', '9'}

        cnt = 0
        for num in range(1,n+1):
            s = str(num)
            is_valid = True
            is_good = False

            for char in s:
                if char not in valid_digit:
                    is_valid = False
                    break
                if char in changing_digit:
                    is_good = True

            if is_good and is_valid:
                cnt += 1
        return cnt