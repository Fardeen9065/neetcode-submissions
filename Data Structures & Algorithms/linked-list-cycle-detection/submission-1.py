# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val = set()
        node = head

        while node:
            if node in val:
                return True
            val.add(node)
            node = node.next

        return False
        
        
        