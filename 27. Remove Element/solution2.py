from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right  = 0, n - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left