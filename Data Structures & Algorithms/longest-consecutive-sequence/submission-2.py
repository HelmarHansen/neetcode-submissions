class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashSet = set(nums)
        res = 1

        for num in hashSet:
            if num - 1 not in hashSet and num + 1 in hashSet:
                pre = 1
                cur = num + 1
                while cur in hashSet:
                    pre += 1
                    cur += 1
                res = max(res, pre)
        return res