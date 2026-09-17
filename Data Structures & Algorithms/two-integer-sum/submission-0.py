class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, m in enumerate(nums):
            for j, n in enumerate(nums):
                if i == j:
                    continue
                if m + n == target:
                    return [i, j]
