#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1, p2 = l1, l2
        dummy = ListNode(0)
        curr = dummy
        
        carry = 0
        
        while p1 or p2 or carry:
            
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        return dummy.next
# @lc code=end

