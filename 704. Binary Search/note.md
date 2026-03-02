# 704. Binary Search

## 題目

給定一個**升序排列**的整數陣列 `nums` 和一個目標值 `target`，  
回傳 `target` 在陣列中的 index，找不到則回傳 `-1`。

---

## 核心概念：二分搜尋

每次取中間值與 target 比較，根據大小縮減搜尋範圍，  
每次迭代淘汰一半的元素。

### 指針定義（閉區間 `[left, right]`）

| 指針 | 初始值 |
|------|--------|
| `left` | `0` |
| `right` | `len(nums) - 1` |

迴圈條件用 `left <= right`（因為右邊界本身也是合法搜尋位置）。

---

## 我的解法

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target == nums[middle]:
                return middle
            else:
                right = middle - 1

        return -1
```

---

## 最佳解法（防止整數溢位）

```python
middle = left + ((right - left) // 2)
```

與 `(left + right) // 2` 數學上等價，但避免了 `left + right` 在語言有整數上限時（如 Java/C++）的溢位問題。  
Python 沒有整數上限，所以兩種寫法結果相同，但**養成這個習慣**在其他語言很重要。

---

## 複雜度分析

| | 複雜度 |
|-|--------|
| 時間 | O(log n) — 每次砍半 |
| 空間 | O(1) — 只用常數變數 |

---

## 易錯點

1. **右邊界初始值**：用閉區間則 `right = len - 1`，用開區間則 `right = len`，兩者迴圈條件不同，不要混用。
2. **middle 更新**：找到 target 時直接 `return middle`，不要繼續縮範圍。
3. **找不到時**：迴圈結束後回傳 `-1`。
