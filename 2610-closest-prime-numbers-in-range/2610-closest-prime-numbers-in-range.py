from typing import List
from math import sqrt

class Solution:
    def IsPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [num for num in range(left, right + 1) if self.IsPrime(num)]
        
        if len(primes) < 2:
            return [-1, -1]  

        min_gap = float('inf')
        ans = [-1, -1]

        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < min_gap:
                min_gap = primes[i] - primes[i - 1]
                ans = [primes[i - 1], primes[i]]
        
        return ans
