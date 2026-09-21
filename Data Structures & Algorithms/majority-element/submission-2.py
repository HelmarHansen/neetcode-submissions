class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        a=int((n/2))
        return nums[a]
        