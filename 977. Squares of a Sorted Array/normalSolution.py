from typing import List

def sortedSquares(self, nums: List[int]) -> List[int]:
    n = [i*i for i in nums]
    n.sort()
    return n