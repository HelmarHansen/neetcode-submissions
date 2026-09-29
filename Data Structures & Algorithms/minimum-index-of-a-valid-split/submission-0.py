from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        dom_val, total_dom_count = Counter(nums).most_common(1)[0]
        
        left_dom_count = 0
        
        for i, val in enumerate(nums[:-1]):
            if val == dom_val:
                left_dom_count += 1
            
            left_len = i + 1
            right_len = n - left_len
            

            right_dom_count = total_dom_count - left_dom_count
            
            if left_dom_count * 2 > left_len and right_dom_count * 2 > right_len:
                return i
                
        return -1
