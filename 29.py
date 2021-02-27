INT_MAX = 2**31-1
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def div(big, small):
            if big < small:
                return 0
            cnt, tmp = 1, small
            while tmp << 1 < big:
                cnt <<= 1
                tmp <<= 1
            return cnt + div(big - tmp, small)
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return min(-dividend, INT_MAX)
        res = div(abs(dividend), abs(divisor))
        if dividend * divisor > 0:
            return min(res, INT_MAX)
        return -res
