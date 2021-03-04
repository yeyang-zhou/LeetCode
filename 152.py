class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = imin = imax = nums[0]
        for num in nums[1:]:
            if num < 0:
                imin, imax = imax, imin
            imin = min(imin * num, num)
            imax = max(imax * num, num)
            res = max(res, imax)
        return res
