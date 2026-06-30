class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod = 1
        if n >= 0:
            for i in range(n):
                prod *= x
        else:
            for i in range(abs(n)):
                prod /= x
        return prod