# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        node = head
        length = 0
        i = 0

        while node:
            length += 1
            node = node.next
        
        length = length - n

        node = head

        if i == length == 0:
            head = node.next
            node.next = None
            return head
        while node:
            if i == length:
                prev.next = node.next
                node.next = None
            prev = node
            i += 1
            node = node.next

        return head

        