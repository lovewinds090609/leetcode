# 59. Spiral Matrix II

## 題目
給定 `n`，生成一個 n×n 矩陣，以螺旋順序填入 1 到 n²。

**Example:** n=3
```
1 2 3
8 9 4
7 6 5
```

## 思路：方向模擬

維護當前方向，每次填完一格後，**看下一格是否可走**：
- 出界 or 已填（!= 0）→ 轉向，並移動到新方向的下一格
- 否則 → 繼續往同方向走

### 關鍵：先寫、再看下一格
```
matrix[y][x] = i       # 先填當前格
if 下一格出界或已填:
    轉向
    移到新方向的起點
else:
    繼續往前走
```

> ⚠️ 不能「先判斷當前格是否是牆再寫值」——最後一格（中心）會因為四周已填而永遠不被寫入。

## 解法

```python
def generateMatrix(self, n: int) -> List[List[int]]:
    right, down, left, up = True, False, False, False
    matrix = [[0] * n for _ in range(n)]
    x, y = 0, 0

    for i in range(1, n * n + 1):
        matrix[y][x] = i  # 先寫

        if right:
            if x + 1 >= n or matrix[y][x+1] != 0:
                right, down = False, True
                y += 1
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
```

## 更簡潔寫法：方向陣列

```python
def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    d = 0
    x, y = 0, 0

    for i in range(1, n * n + 1):
        matrix[x][y] = i
        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4  # 轉向
            x, y = x + dirs[d][0], y + dirs[d][1]

    return matrix
```

## 複雜度
| | |
|---|---|
| Time | O(n²) — 每格填一次 |
| Space | O(1) extra — 不計輸出矩陣 |

## 踩過的坑

| 問題 | 原因 |
|------|------|
| 先判斷再寫，中心格填不到 | 最後一格四周都已填，hit_wall=True，值永遠寫不進去 |
| `i` 從 0 開始 | 0 和空格相同，無法用 `!= 0` 判斷是否已填 |
| `or` 順序錯誤 | `matrix[y][x]` 要放在邊界判斷後面，否則 index out of range |
| 各方向邊界搞混 | right 查 `x+1>=n`，down 查 `y+1>=n`，left 查 `x-1<0`，up 查 `y-1<0` |
