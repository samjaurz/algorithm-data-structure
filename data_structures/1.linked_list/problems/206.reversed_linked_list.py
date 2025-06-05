from typing import Optional
           
class ListNode:
    def __init__(self,data):
       self.data = data
       self.next = None

def create_linked_list(nums:list) ->Optional[ListNode]:
    if not nums:
      return None
   
    head = ListNode(nums[0])
    current = head

    for value in nums[1:]:
       current.next = ListNode(value)
       current = current.next
    
    return head

def print_linked_list(LL:Optional[ListNode]) -> str:
    current = LL
    while current:
        print(current.data, end = "->")
        current =current.next
    print("None")

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current is not None:
           save_value = current.next
           current.next = prev
           prev = current
           current = save_value
        
        return prev
    

if __name__ == '__main__':
    
    ll1 = create_linked_list([1,2,3,4,5])
    ll2 = create_linked_list([1,2])
    ll3 = create_linked_list([])

    reversed1 = Solution().reverseList(ll1)
    reversed2 = Solution().reverseList(ll2)
    reversed3 = Solution().reverseList(ll3)

    print_linked_list(reversed1)
    print_linked_list(reversed2)
    print_linked_list(reversed3)