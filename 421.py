class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = mask = 0
        for i in range(30, -1, -1):
            mask |= (1 << i)
            tmp = res | (1 << i)
            s = {num & mask for num in nums}
            for prefix in s:
                if prefix ^ tmp in s:
                    res = tmp
                    break
        return res
