# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the starting anchor
        dummy = ListNode(0)
        temp3 = dummy
        
        temp1 = list1
        temp2 = list2
        
        # 2. Compare elements from both lists and link the smaller one
        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
            temp3 = temp3.next
            
        # 3. Append any remaining nodes left over in either list
        if temp1 is not None:
            temp3.next = temp1
        elif temp2 is not None:
            temp3.next = temp2
            
        # 4. Return the head of the real merged list (skipping the dummy)
        return dummy.next