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

        for i in range(1, n * n + 1):
            matrix[y][x] = i  # 先寫
            if right:
                if x + 1 >= n or matrix[y][x+1] != 0:  # 看下一格
                    right, down = False, True
                    y += 1   # 轉向後的起始位移
                else:
                    x += 1
            elif down:
                if y + 1 >= n or matrix[y+1][x] != 0:
                    down, left = False, True
                    x -= 1
                else:
                    y += 1  
            elif left:
                if x - 1 < 0 or matrix[y][x-1] != 0:
                    left, up = False, True
                    y -= 1
                else:
                    x -= 1
            elif up:
                if y - 1 < 0 or matrix[y-1][x] != 0:
                    up, right = False, True
                    x += 1
                else:
                    y -= 1

        return matrix