#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.traversal(root,a)
        return a
    def traversal(self, root, a):
        if not root:
            return 
        self.traversal(root.left,a)
        a.append(root.val)
        self.traversal(root.right,a)
    
# @lc code=end

