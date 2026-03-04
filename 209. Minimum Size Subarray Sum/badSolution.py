from typing import List

#第一次寫的解法 複雜度 O(N^2) Runtime Error
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = len(nums) - 1
        pointer = cur
        minimal = 100001
        total = 0

        while pointer >= 0:
            total += nums[pointer]
            if total >= target:
                if (cur - pointer + 1)  < minimal:
                    minimal = cur - pointer + 1
                cur -= 1
                pointer = cur
                total = 0
                continue
            pointer -= 1
        
        if minimal != 100001:
            return minimal
        else:
            return 0