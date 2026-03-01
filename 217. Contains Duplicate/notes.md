# 217. Contains Duplicate

## 題目
給定一個整數陣列 `nums`，如果陣列中有任何值出現**至少兩次**，回傳 `true`；若所有元素都不重複，回傳 `false`。

---

## My Solution（排序後線性掃描）

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pre = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num == pre:
                return True
            pre = num
        return False
```

### 思路
先將陣列排序，排序後重複的元素一定相鄰，接著線性掃描，比較每個元素與前一個是否相同。

### 複雜度分析

| | 複雜度 | 說明 |
|---|---|---|
| **時間** | O(n log n) | 瓶頸在 `sort()`，排序需要 O(n log n) |
| **空間** | O(1) | 只用了 `pre` 一個額外變數（排序為 in-place） |

---

## Best Solution（Hash Set）

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

### 思路
將陣列轉成 `set`，`set` 會自動去除重複元素。若轉換後長度變短，代表有重複元素存在。

### 複雜度分析

| | 複雜度 | 說明 |
|---|---|---|
| **時間** | O(n) | 建 `set` 需要遍歷整個陣列，每次 insert 平均 O(1) |
| **空間** | O(n) | 最差情況（無重複）`set` 會存下所有 n 個元素 |

---

## 比較總結

| | My Solution | Best Solution |
|---|---|---|
| **時間複雜度** | O(n log n) | ✅ O(n) |
| **空間複雜度** | ✅ O(1) | O(n) |
| **可讀性** | 普通 | ✅ 極簡 |

> **結論**：Best Solution 用空間換時間，時間複雜度更優。
> My Solution 則是不額外用記憶體的做法，是一種 space-optimized 的思路，但時間複雜度較差。
> 若記憶體不是瓶頸，優先選 Hash Set 解法。
