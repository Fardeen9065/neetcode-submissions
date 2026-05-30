# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        num1 = ""
        num2 = ""

        while head1:
            num1 += str(head1.val)
            head1 = head1.next

        while head2:
            num2 += str(head2.val)
            head2 = head2.next

        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = float(num1) + float(num2)
        ans = int(ans)
        print(num1,num2)
        print(ans)
        ans = str(ans)
        ans = list(ans[::-1])
        print(ans)
        dummy = ListNode(0)
        curr = dummy

        for i in ans:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next
