from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums : List[int] = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        index = right
        while left <= right:
            if((nums[left] * nums[left]) >= (nums[right] * nums[right])):
                newNums[index] = nums[left] * nums[left]
                index-=1
                left+=1
            else:
                newNums[index] = nums[right] * nums[right]
                index-=1
                right-=1

        return newNums