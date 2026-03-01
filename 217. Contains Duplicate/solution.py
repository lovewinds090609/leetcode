from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pre = nums[0]
        for i,num in enumerate(nums):
            if i == 0:
                continue
            if num == pre:
                return True
            pre = num
        return False