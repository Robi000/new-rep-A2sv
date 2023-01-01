class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set(list(range(0, len(nums) + 1)))
        for x in nums:
            num.remove(x)
        return (num.pop())
            
        