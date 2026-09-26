from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        preFreq = defaultdict(int)
        preFreq[0] = 1

        res = 0

        for num in nums:
            pre += num
            res += preFreq[pre - k]
            preFreq[pre] += 1
        
        return res