# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast , slow = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, slow, prev.next = slow , slow.next , None 
        while slow:
            slow.next , prev , slow = prev , slow , slow.next
        
        head1 = head
        head2 = prev
        
        while head2:
            if head1.val != head2.val : return False
            head1= head1.next
            head2 = head2.next
        return True
            
        