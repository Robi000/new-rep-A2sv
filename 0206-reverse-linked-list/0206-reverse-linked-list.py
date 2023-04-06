# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursiv(self , node):
        if node.next == None:
            return (node , node)
        else:
            ans = self.recursiv(node.next)
            target = ans[0]
            target.next = node
            return (node , ans[1])
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        newhead = None
        ans = self.recursiv(head)
        ans[0].next = None
        
        return ans[1]
        