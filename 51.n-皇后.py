#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    
    def __init__(self) -> None:
        self.res = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.res
    
    def backtrack(self, board, row):
        if row  == len(board):
            self.res.append([''.join(row) for row in board])
            return
    
    
    
    
#   def solveNQueens(self, n):
#     def DFS(queens, xy_dif, xy_sum):
#         p = len(queens)
#         if p==n:
#             result.append(queens)
#             return None
#         for q in range(n):
#             if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
#                 DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
#     result = []
#     DFS([],[],[])
#     return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

# @lc code=end

