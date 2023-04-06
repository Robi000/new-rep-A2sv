# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        while head:
            if head.next:
                if head.next.val in nums and head.val in nums:
                    ans += 1
                    while head.next.val in nums:
                        nums.remove(head.val)
                        head = head.next
                        if head.next == None:
                            break
                    nums.remove(head.val)
                    
            head = head.next
        ans = ans + len(nums)
        return ans