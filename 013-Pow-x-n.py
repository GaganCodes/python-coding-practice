class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1.0
            elif exponent % 2 == 0:
                # Crucial to divide by 2 because of divide and conquer theme
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f
