class Solution:
    # use mod and div to get digits, use set to store seen,
    def isHappy(self, n: int) -> bool:
        def getDigits(n):
            digits = []
            while n > 9:
                digits.append(n % 10)
                n = n // 10
            digits.append(n)
            return digits
        seen = {n}
        while n != 1:
            n = sum(map(lambda x: x**2, getDigits(n)))
            if n in seen:
                return False
            seen.add(n)
        return True