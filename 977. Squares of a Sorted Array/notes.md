# 977. Squares of a Sorted Array

## 題目
給一個**已排序（非遞減）**的整數陣列 `nums`，回傳每個數字平方後排序好的新陣列。

**範例：**
```
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
```

---

## 解法一：雙指標（最佳解）✅

**時間複雜度：O(N)　空間複雜度：O(N)**

### 核心思路
- 因為原陣列已排序，平方後的最大值一定在**最左邊（絕對值最大的負數）**或**最右邊（最大的正數）**。
- 用 `left`、`right` 兩個指標夾擠，每次挑出較大的平方值，**從後往前**填入結果陣列。

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums: List[int] = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        index = right
        while left <= right:
            if (nums[left] * nums[left]) >= (nums[right] * nums[right]):
                newNums[index] = nums[left] * nums[left]
                index -= 1
                left += 1
            else:
                newNums[index] = nums[right] * nums[right]
                index -= 1
                right -= 1
        return newNums
```

---

## 解法二：暴力排序（寫法簡潔但較慢）

**時間複雜度：O(N log N)　空間複雜度：O(N)**

### 核心思路
先全部平方，再丟給內建排序。沒有利用到「已排序」的條件。

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = [i * i for i in nums]
        n.sort()
        return n
```

---

## 比較

| | 解法一（雙指標） | 解法二（暴力排序）|
|---|---|---|
| 時間複雜度 | **O(N)** | O(N log N) |
| 利用已排序特性 | ✅ 有 | ❌ 無 |
| 適合場景 | 面試、效能要求高 | 快速實作 |

---

## 關鍵觀念
- 雙指標的核心：**有序陣列的兩端是極端值**，利用這點可把排序步驟省掉。
- `list[None]` ≠ `List[int]`，初始化陣列要用 `[0] * n`，不能用 `[None] * n`。
