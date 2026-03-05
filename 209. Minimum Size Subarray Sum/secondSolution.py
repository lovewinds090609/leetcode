from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minimal = float('inf')
        total = 0
        left = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                total -= nums[left]
                minimal = min(minimal, i - left + 1)
                left += 1

        if(minimal != float('inf')):
            return int(minimal)
        else:
            return 0