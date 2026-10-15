class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        print("nums:", nums)

        for i in range(len(nums)):
            needed = -nums[i]
            print("needed:", needed)
            j, k = 0, len(nums) - 1
            while j < k - 1:
                if j == i:
                    j += 1
                if k == i:
                    k -= 1
                #print("j, k:", nums[j], nums[k])
                current = nums[j] + nums[k]
                if current < needed:
                    j += 1
                elif current > needed:
                    k -= 1
                else:
                    #print("found:", tuple(sorted([nums[i], nums[j], nums[k]])))
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1

        return [list(e) for e in res]          
                