#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 回溯
        
        
        
        # # 动态规划
        # if not root:
        #     return 0
        # maxLeft = self.maxDepth(root.left)
        # maxRight = self.maxDepth(root.right)
        # return max(maxLeft, maxRight) + 1
        
    #     self.maxd = 0
    #     self.curd = 0
    #     self.traverse(root)
    #     return self.maxd
    
    # def traverse(self, root):
        
    #     if not root:
    #         return 
    #     self.curd += 1
    #     if not root.left and not root.right:
    #         self.maxd = max(self.maxd, self.curd)
    #     self.traverse(root.left)
    #     self.traverse(root.right)
    #     self.curd -= 1
        
        
        # if not root:
        #     return
        # maxDepth(root.left)
        
        # maxDepth(root.right)
        
# @lc code=end

