# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLinkedListItems(self, l: Optional[ListNode]) -> List[int]:
        new_list = []
        current = l
        while(current):
            new_list.append(current.val)
            current = current.next
        return new_list  

    def insertAtBeginning(self, prev: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_node = ListNode(n)
        new_node.next = prev
        return new_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = self.getLinkedListItems(l1)
        l2_num = self.getLinkedListItems(l2)
        l1_num.reverse()
        l2_num.reverse()
        l1_int = int("".join(map(str, l1_num)))
        l2_int = int("".join(map(str, l2_num)))

        s = l1_int + l2_int
        s_num = [int(digits) for digits in str(s)]

        prev = None
        for i in range(len(s_num)):
            prev = self.insertAtBeginning(prev, s_num[i])
        
        return prev