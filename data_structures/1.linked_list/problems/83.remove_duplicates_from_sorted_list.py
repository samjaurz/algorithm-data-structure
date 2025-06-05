from typing import Optional

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(linked):
    if not linked:
        return None
    
    head = ListNode(linked[0])
    current = head

    for value in linked[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head

if __name__ == '__main__':
    ll1 = create_linked_list([1,1,2])
    ll2 = create_linked_list([1,1,2,3,3])

    print("Original ll1: ")
    print_list(ll1)
    print("After removing duplicates:")
    print_list(Solution().deleteDuplicates(ll1))

    print("\nOriginal ll2: ")
    print_list(ll2)
    print("After removing duplicates:")
    r = Solution().deleteDuplicates(ll2)
    print_list(r)
