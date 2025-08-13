class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        r = x
        # Integer Newton iteration: r_{k+1} = floor((r_k + x // r_k) / 2)
        # Invariant: r*r >= x; loop stops when r is the floor(sqrt(x)).
        while r * r > x:
            r = (r + x // r) // 2
        return r
