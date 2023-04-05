# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        dic = defaultdict(set)
        while head.next != None:
            if head in dic[head.val]:
                return True
            dic[head.val].add(head)
            head = head.next
        return False
            
            
            
        