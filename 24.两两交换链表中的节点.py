#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            
            temp = temp.next.next
        return dummy.next
        
        
        # 错误2
        # dummy = ListNode(0)
        # dummy.next = head
        # temp = dummy
        # if temp.next or temp.next.next:
        #     p1,p2 = temp.next, temp.next.next
        # else:
        #     return dummy.next
        
        # while p1 and p2:
        #     p1.next = p2.next
        #     p2.next = p1
        #     temp.next = p2
            
        #     p1,p2 = temp.next, temp.next.next
        #     if temp.next.next  or p1.next.next or p2.next.next:

        #         temp = temp.next.next
        #         p1 = p1.next.next
        #         p2 = p2.next.next
        #     else:
        #         break
            
            
        # return dummy.next
            
        
        
        # 错误的解法 
        # p1,p2,p3 = head,head,head
        # if p1.next:
        #     p2 = p1.next
        # else:
        #     return head
        # if p2.next:
        #     p3 = p2.next
            
        # while p2:
        #     p1.next = p2.next
        #     p2.next = p1
        #     if p3:
        #         p1.next = p3
        #     if p3.next:
        #         p2 = p3.next
        #     if p2.next:
        #         p3 = p2.next
            
        # return head
        
# @lc code=end

