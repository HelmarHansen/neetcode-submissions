class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < len(nums):
            print(nums[i], nums[i - 1])
            if nums[i] == nums[i - 1]:
                print("pop")
                nums.pop(i)
                continue
            i += 1
        return len(nums)