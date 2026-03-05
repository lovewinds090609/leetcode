from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        right,down,left,up = True,False,False,False
        matrix : List[List[int]] = []
        for _ in range(n):       # 外層：跑 rows 次
            row : List[int] = []
            for _ in range(n):   # 內層：跑 cols 次
                row.append(0)
            matrix.append(row)
        
        x,y = 0,0

        for i in range(n * n):
            while right:
                if(matrix[y][x] != 0):
                    right = False
                    down = True
                if(x == n):
                    x -= 1
                else:
                    x += 1    
                
            while down:

            while left:

            while up:

        return matrix