# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        queue = [root]
        ans = [root.val]
        print(ans)

        while queue:
            node = queue.pop(0)
            if node.left:
                ans.append(node.left.val)
                queue.append(node.left)
            if node.right:
                ans.append(node.right.val)
                queue.append(node.right)
        ans.sort()
        print(ans)
        return ans[k-1]
        