class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums) -1
        i = 0
        while i < len(nums)-1:
            if nums[i]== nums[i + 1]:
                nums.remove(nums[i])
                leng -= 1
            else:
                i += 1
        return len(nums)
        