# 209. Minimum Size Subarray Sum

## 題目

給定一個由**正整數**組成的陣列 `nums` 和正整數 `target`，  
找出長度**最小**的連續子陣列，使其元素總和 `>= target`，回傳其長度。  
找不到則回傳 `0`。

---

## 解法一：暴力 O(N²)（`badSolution.py`）

從每個位置往左掃，累加直到 `>= target`，記錄最小長度。

```python
cur = len(nums) - 1
pointer = cur
minimal = 100001
total = 0

while pointer >= 0:
    total += nums[pointer]
    if total >= target:
        if (cur - pointer + 1) < minimal:
            minimal = cur - pointer + 1
        cur -= 1
        pointer = cur
        total = 0
        continue
    pointer -= 1

return minimal if minimal != 100001 else 0
```

**問題**：雙層邏輯混亂，且本質上是 O(N²)，LeetCode 判 TLE / Runtime Error。

---

## 解法二：滑動視窗 O(N)（`secondSolution.py`）

維護一個可伸縮的視窗 `[left, i]`，右指針 `i` 不斷往右擴展加入元素，  
當 `total >= target` 時，嘗試從左縮小視窗並更新最小長度，直到 `total < target`。

```python
minimal = float('inf')
total = 0
left = 0

for i in range(len(nums)):
    total += nums[i]
    while total >= target:
        total -= nums[left]
        minimal = min(minimal, i - left + 1)
        left += 1

return int(minimal) if minimal != float('inf') else 0
```

### 關鍵：為何先縮再更新不行？

縮小的順序是：**先記錄長度，再移動 left**。  
`i - left + 1` 在 `left += 1` 之前計算，才是當前視窗長度。

---

## 複雜度分析

| | 複雜度 |
|-|--------|
| 時間 | O(N) — 每個元素最多進出視窗各一次 |
| 空間 | O(1) — 只用常數變數 |

---

## 易錯點

1. **`float('inf')` 回傳型別**：函式標注 `-> int`，回傳時需加 `int()` 強轉，否則 Pylance 報型別錯誤。
2. **縮視窗的時機**：`while total >= target` 而非 `if`，因為縮一次後可能仍 `>= target`，要持續縮到最小。
3. **視窗長度公式**：`i - left + 1`，注意是閉區間兩端都包含。
