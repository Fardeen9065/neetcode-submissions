# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,max_num):
            if not node:
                return 0
            if node.val >= max_num:
                res = 1
            else:
                res = 0
            max_num = max(max_num,node.val)
            res += dfs(node.left,max_num)
            res += dfs(node.right,max_num)
            return res
        return dfs(root,root.val)

       
        