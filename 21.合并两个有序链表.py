#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针
        dummy = ListNode(-1)
        p = dummy
        q1, q2= list1, list2
        while q1 and q2:
            if q1.val < q2.val:
                p.next = q1
                q1 = q1.next
            else :
                p.next = q2
                q2 = q2.next
            p = p.next
        while q1:
            p.next = q1
            q1 = q1.next
            p = p.next
        while q2:
            p.next = q2
            q2 = q2.next
            p = p.next
        return dummy.next
                
# @lc code=end

