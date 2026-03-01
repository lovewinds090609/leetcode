# 242. Valid Anagram

## 題目

給定兩個字串 `s` 和 `t`，判斷 `t` 是否為 `s` 的 anagram（字母異位詞）。

---

## 方法比較

### My Solution — 手動 HashMap

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d_s = {}
        d_t = {}
        for i in range(len(s)):
            d_s[s[i]] = d_s.get(s[i], 0) + 1
            d_t[t[i]] = d_t.get(t[i], 0) + 1

        return d_s == d_t
```

### Best Solution — `collections.Counter`

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

---

## 複雜度比較

|          | My Solution | Counter Solution |
| -------- | ----------- | ---------------- |
| **Time** | O(n)        | O(n)             |
| **Space** | O(k)       | O(k)             |

> `n` = 字串長度，`k` = unique 字元數（英文字母最多 26，可視為 O(1)）

**本質相同**：兩者都是掃一遍建 hash map，再比對兩個 map。

---

## 關鍵差異

| 面向 | My Solution | Counter Solution |
|------|-------------|------------------|
| Big-O | 相同 | 相同 |
| 常數因子 | 純 Python，稍慢 | C 實作，較快 |
| 可讀性 | 較冗長 | 一行搞定 |
| 學習價值 | 高（理解底層邏輯） | 低（隱藏細節） |

---

## Counter 底層原理

`Counter` 是 `dict` 的子類別，底層等同於：

```python
for elem in iterable:
    self[elem] = self.get(elem, 0) + 1
```

- 不存在的 key 不會拋 `KeyError`，`__missing__` 直接回傳 `0`
- 比較兩個 `Counter` 就是比較兩個 `dict` 的所有 key-value pair

---

## 重點 Takeaway

- 面試建議先說 `Counter` 解法，再解釋底層等同於 HashMap 計數
- `dict.get(key, 0)` 是手動版 Counter 的核心技巧，避免 `None` 的型別錯誤
