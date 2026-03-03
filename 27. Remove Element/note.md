# LeetCode 27: Remove Element

- **題型**：In-place 陣列原地修改
- **核心概念**：雙指針
- **題目不要求**維護剩餘元素的相對順序

---

## ✅ 主推解法：快慢指針 (Fast/Slow Pointers)

**常見度：** ⭐⭐⭐⭐⭐

### 思路

| 指針 | 角色 |
|------|------|
| `fast` | 偵查兵，掃描找出「合法元素」（不等於 `val`） |
| `slow` | 標記下一個可寫入的位置 |

- `fast` 找到合法元素 → 複製到 `slow` 位置，`slow += 1`
- `fast` 遇到目標 `val` → 直接跳過
- 最終 `slow` 的值 = 新陣列長度

### 程式碼

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

### 複雜度
- **Time:** O(n)
- **Space:** O(1)

### 相關題型
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) — 同樣的快慢指針思路

---

## 🔁 變體解法：雙向夾擊 (Two Pointers - Alternate)

**常見度：** ⭐⭐⭐

### 思路

| 指針 | 角色 |
|------|------|
| `left` | 從頭掃，找出需要被移除的 `val` |
| `right` | 從尾掃，找出正常元素準備蓋掉 `val` |

- `left` 找到 `val`，`right` 找到正常元素 → 用右邊覆蓋左邊
- **會打亂元素相對順序**，但本題不要求順序
- 優勢：`val` 數量極少時，減少不必要的覆寫操作

### 程式碼

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left
```

### 複雜度
- **Time:** O(n)
- **Space:** O(1)

### 相關題型
- [344. Reverse String](https://leetcode.com/problems/reverse-string/) — 首尾夾擊經典
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — 夾擊尋找加總

---

## 📌 總結

| | 快慢指針 | 雙向夾擊 |
|---|---|---|
| 保持元素順序 | ✅ 是 | ❌ 否 |
| 推薦程度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 記憶難度 | 低 | 中 |
| 泛用性 | 高（可套用 LC26） | 低（特定場景才有優勢） |
