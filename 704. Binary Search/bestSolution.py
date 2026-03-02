from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        left = 0
        right = lens-1

        while left <= right:
            middle = left + ((right - left) // 2)
            if target > nums[middle]:
                left = middle + 1
            elif target == nums[middle]:
                return middle
            else:
                right = middle - 1
        
        return -1