class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            needed = -nums[i]
            j, k = 0, len(nums) - 1
            while j < k - 1:
                if j == i:
                    j += 1
                if k == i:
                    k -= 1
                current = nums[j] + nums[k]
                if current < needed:
                    j += 1
                elif current > needed:
                    k -= 1
                else:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1

        return [list(e) for e in res]          
                