class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        d = {length - 1: 1}
        suffix = 1
        prefix = 1
        res = []
        for inx in range(length - 2, -1, -1):
            suf = nums[inx + 1] * suffix
            suffix = suf
            d[inx] = suf

        for inx in range(len(nums)):
            suf = d[inx]
            prod = prefix * suf
            prefix *= nums[inx]
            res.append(prod)

        return res
