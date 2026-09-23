class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False

        for i in range(len(nums)):
            print((i + 1) % len(nums))
            if nums[i] <= nums[(i + 1) % len(nums)]:
                continue
            if rotated:
                return False
            rotated = True
        return True