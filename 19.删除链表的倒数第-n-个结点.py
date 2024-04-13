#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        q = self.findFromEnd(dummy,n+1)
        q.next = q.next.next
        return dummy.next  
        # 先让p2先走n步
        # for _ in range(n):
        #     p2 = p2.next
            
        # while p2:
        #     if p2.next == None:
        #         q = p1
        #     p1 = p1.next
        #     p2 = p2.next
            
        
    def findFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head
        for _ in range(n):
            p2 = p2.next
        while p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        
# @lc code=end

