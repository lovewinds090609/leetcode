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

        for i in range(1,n * n + 1):
            while right:
                hit_wall = (x == n or matrix[y][x] != 0)
                if hit_wall:
                    right = False
                    down = True
                else:
                    matrix[y][x] = i
                if hit_wall:
                    x -= 1
                    y += 1
                else:
                    x += 1    
                    break
            while down:
                hit_wall = (y == n or matrix[y][x] != 0)
                if hit_wall:
                    down = False
                    left = True
                else:
                    matrix[y][x] = i
                if hit_wall:
                    y -= 1
                    x -= 1
                else:
                    y += 1 
                    break
            while left:
                hit_wall = (x == -1 or matrix[y][x] != 0)
                if hit_wall:
                    left = False
                    up = True
                else:
                    matrix[y][x] = i
                if hit_wall:
                    x += 1
                    y -= 1
                else:
                    x -= 1 
                    break
            while up:
                hit_wall = (y == -1 or matrix[y][x] != 0)
                if hit_wall:
                    up = False
                    right = True
                else:
                    matrix[y][x] = i
                if hit_wall:
                    y += 1
                    x += 1
                else:
                    y -= 1 
                    break

        return matrix