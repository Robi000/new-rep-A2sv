class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
            i += 1
        return nums