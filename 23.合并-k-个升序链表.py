#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(-1)
        p =dummy
        
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(pq, (node.next.val,id(node.next) , node.next))
        return dummy.next
        
        
        
            
        
        
# @lc code=end

