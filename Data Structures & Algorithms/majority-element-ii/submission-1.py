class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, can2 = -1, -1
        n1, n2 = 0, 0

        for num in nums:
            if can1 == num:
                n1 += 1
            elif can2 == num:
                n2 += 1
            else:
                if n1 == 0:
                    can1 = num
                    n1 += 1
                elif n2 == 0:
                    can2 = num
                    n2 += 1
                else:
                    n1 -= 1
                    n2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            count1 += 1 if num == can1 else 0
            count2 += 1 if num == can2 else 0

        res = []
        margin = len(nums) // 3
        if count1 > margin:
            res.append(can1)
        if count2 > margin:
            res.append(can2)
        
        return res
            