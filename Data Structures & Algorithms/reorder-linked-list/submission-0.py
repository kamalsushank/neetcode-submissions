class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(s):
            curr = s
            pre = None

            while curr:
                post = curr.next
                curr.next = pre
                pre = curr
                curr = post

            return pre

        if not head or not head.next:
            return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        c2 = slow.next
        slow.next = None

        c2 = reverse(c2)

        c1 = head

        while c1 and c2:
            temp1 = c1.next
            temp2 = c2.next

            c1.next = c2
            c2.next = temp1

            c1 = temp1
            c2 = temp2