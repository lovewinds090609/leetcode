# 203. Remove Linked List Elements

## 題目
移除 linked list 中所有值等於 `val` 的節點，回傳新的 head。

## 核心觀念：Dummy Node

刪除節點需要知道「前一個節點」才能跳過它：
```
cur.next = cur.next.next  # 跳過 cur.next，等於刪掉它
```

問題：如果 `head` 本身就要被刪，就沒有「前一個節點」。

**解法**：在 list 最前面加一個假節點 `dummy`，讓 `cur` 從 `dummy` 開始走，這樣所有節點（包含原本的 head）都有前一個節點可以操作。

## 最佳解法

```python
def removeElements(self, head, val):
    dummy = ListNode(0)  # 假節點，值無所謂
    dummy.next = head
    cur = dummy          # cur 永遠指向「要刪節點的前一個」

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next  # 跳過，等於刪除
        else:
            cur = cur.next            # 不刪才往前走

    return dummy.next  # dummy 的下一個才是真正的 head
```

- **Time**: O(n)
- **Space**: O(1)

## 第一次解法的問題

同時用 `head` 和 `cur` 兩個指標，邏輯混亂：

1. `if head.val == val` 在迴圈裡每次都重新判斷固定的 `head`，邏輯錯亂
2. `cur.next.val` 在 `cur.next is None` 時會 crash
3. 刪掉 head 後 `cur` 和 `head` 同步關係不對

## 重點

- 只要「需要記住前一個節點」就用 dummy node
- `cur` **不刪才走**，刪了不走（因為 `cur.next` 已換成下一個節點）
