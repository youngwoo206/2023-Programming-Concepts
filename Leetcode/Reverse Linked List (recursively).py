'''
Given the head of a singly linked list, reverse the list, and return the reversed li
'''


def reverseList(self, head):
    if not head:
        return None

    newHead = head

    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head

    head.next = None

    return newHead

#time: O(n)
#space: O(n)
