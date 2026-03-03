from typing import List

class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        #定義區間[0,len(nums)) 左閉右開 ->right只是邊界 所以left == right時是不合法的
        left = 0
        right = len(nums)

        while left < right:
            middle = left + ((right - left) // 2)
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle
            else:
                return middle

        return -1