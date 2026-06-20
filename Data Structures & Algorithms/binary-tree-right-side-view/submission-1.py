# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = [(root.val,0)]
        queue = [root]
        depth = 1

        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                node = queue.pop(0)
                left = node.left
                right = node.right
                if left:
                    ans.append((left.val,depth))
                    queue.append(left)
                if right:
                    ans.append((right.val,depth))
                    queue.append(right)
            depth += 1
        res = []
        for idx in range(len(ans)-1):
            if ans[idx][1] != ans[idx+1][1]:
                res.append(ans[idx][0])
        res.append(ans[-1][0])
        return res



        