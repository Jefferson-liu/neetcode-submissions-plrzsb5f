class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod = 1
        if n >= 0:
            for i in range(n//2):
                prod *= x * x
            if n % 2 == 1:
                prod *= x
        else:
            for i in range(abs(n) // 2):
                prod /= (x * x)
            if n % 2 == 1:
                prod /= x
        return prod