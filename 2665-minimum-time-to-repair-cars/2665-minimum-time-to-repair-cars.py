class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(t):
            total_cars = 0
            for r in ranks:
                total_cars += int((t // r) ** 0.5)
                if total_cars >= cars:
                    return True
            return False

        left, right = 1, min(ranks) * (cars ** 2)
        while left < right:
            mid = (left + right) // 2
            if can_repair(mid):
                right = mid
            else:
                left = mid + 1
        
        return left