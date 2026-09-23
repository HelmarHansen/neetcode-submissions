class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, L, R = 0, 0, len(nums) - 1
        while i <= R:
            value = nums[i]
            if value == 0:
                nums[i] = nums[L]
                nums[L] = value
                L += 1
                i += 1
            elif value == 2:
                nums[i] = nums[R]
                nums[R] = value
                R -= 1
            else:
                i += 1
        